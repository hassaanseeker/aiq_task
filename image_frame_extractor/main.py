from etl.insert_resized_images import insert_resized_image_df
from sqlite.sqlite_conn import get_sqlite_conn

if __name__ == '__main__':

    insert_resized_image_df(file_path='/Users/muhammadhassaanrafique/aiq_task/image_transf_task/data/images_data.csv')
    