import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('aiq_image_task.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define the table name you want to drop
table_to_drop = 'resized_image_data'

# Construct the DROP TABLE query
drop_table_query = f'DROP TABLE IF EXISTS {table_to_drop};'

# Execute the DROP TABLE query
cursor.execute(drop_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()