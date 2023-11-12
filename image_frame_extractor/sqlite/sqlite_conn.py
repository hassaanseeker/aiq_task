import sqlite3

def get_sqlite_conn():
    conn = sqlite3.connect('/Users/muhammadhassaanrafique/aiq_task/image_transf_task/aiq_image_task.db')
    
    return conn