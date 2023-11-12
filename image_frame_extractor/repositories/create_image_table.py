import sys
sys.path.append('/Users/muhammadhassaanrafique/aiq_task/image_transf_task')
from sqlite.sqlite_conn import get_sqlite_conn

conn = get_sqlite_conn()

def create_image_table_sql():
    """
    Function to create table for the resize image.
    """

    col_str = ''
    for i in range(0, 150):
        col_str += 'col' + str(i) + ' INTEGER, '

    # Remove the trailing comma and space
    col_str = col_str[:-2]
    col_str += ', depth FLOAT'

    # Use col_str in your SQL query
    sql_query = f"CREATE TABLE resized_image_data ({col_str});"

    cursor = conn.cursor()
    cursor.execute(sql_query)

    conn.commit()
    conn.close()

if __name__ == '__main__':

    create_image_table_sql()