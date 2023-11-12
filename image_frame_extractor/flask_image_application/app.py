from flask import Flask, render_template, request
from PIL import Image
import base64
import io
import numpy as np
import pandas as pd
import sqlite3
app = Flask(__name__)

def get_resized_image():
    """
    Function to get the image frames data from sqlite databse.
    """
    conn = sqlite3.connect('/app/aiq_image_task.db')  # Replace 'your_database.db' with the actual name of your SQLite database

    # Write your SQL query
    sql_query = "SELECT * FROM resized_image_data"  # Replace 'your_table_name' with the actual name of your table

    # Use the read_sql_query function to execute the query and fetch the data into a DataFrame
    df = pd.read_sql_query(sql_query, conn)
    conn.close()

    # Assuming 'image_data' is a 2D numpy array with shape (5400, 200)
    # You can replace this with your actual image data
    df['depth'] = df['depth'].astype('float')
    print(max_depth, min_depth,df['depth'])
    df = df[(df['depth'] >= min_depth) & (df['depth'] <= max_depth)].reset_index(drop = True)
    pixels = df.drop(columns='depth')
    pixels = pixels.astype(np.uint8)
    print(pixels)
    image_data = pixels.values

    # Create a Pillow Image object
    image = Image.fromarray(image_data)
    data = io.BytesIO()
    image.save(data, "JPEG")
    encoded_img_data = base64.b64encode(data.getvalue())

    return encoded_img_data

@app.route('/')
def render_index():
    """
    Function to render the html template.
    """    
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    """
    Function that returns the frame of the image
    based on the minimum depth and maximum depth input
    from the UI.
    """

    min_depth = float(request.form['min_depth'])
    max_depth = float(request.form['max_depth'])

    encoded_img_data = get_resized_image()

    return render_template('index.html', img_data=encoded_img_data.decode('utf-8'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
