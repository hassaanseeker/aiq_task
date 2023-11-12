import pandas as pd
import numpy as np
from PIL import Image

import sys

sys.path.append('/Users/muhammadhassaanrafique/aiq_task/image_transf_task')

from repositories.insert_resized_images import insert_resized_image_data
from sqlite.sqlite_conn import get_sqlite_conn

def get_image_data(file_path):
    """
    Function that reads the original image data provide in the task.

    Parameters
    ----------
    file_path: absolute path to the image csv file shared for the task.
    """

    images_df = pd.read_csv(file_path)
    pixels = images_df.drop(columns='depth', axis=1)
    depth = images_df['depth']

    return pixels, depth


def resize_image(file_path):
    """
    Function that reduces the width of the provide image from 200 to 150.
    
    Parameters
    ----------
    file_path: absolute path to the image csv file shared for the task.
    """

    pixels, depth = get_image_data(file_path)

    pixels = pixels.astype(np.uint8)
    image_data = pixels.values

    # Create a Pillow Image object
    original_image = Image.fromarray(image_data)

    # Resize the image to a width of 150 and keep the height the same
    resized_width = 150
    resized_image = original_image.resize((resized_width, original_image.height))

    resized_image_df = pd.DataFrame(np.array(resized_image))
    resized_image_df.columns = ['col'+str(x) for x in resized_image_df.columns]
    resized_image_df['depth'] = depth
    print(resized_image_df.head())

    return resized_image_df

def insert_resized_image_df(file_path):
    """
    Function that inserts the resized image data from 150 to 200
    inside the table of sqlite database.

    Parameters
    ----------
    file_path: absolute path to the image csv file shared for the task.
    """

    resized_image_df = resize_image(file_path)
    
    conn = get_sqlite_conn()
    cursor = conn.cursor()

    for i in range(0,resized_image_df.shape[0]):
        cursor.execute(insert_resized_image_data(), resized_image_df.loc[i].values)

    conn.commit()
    conn.close()