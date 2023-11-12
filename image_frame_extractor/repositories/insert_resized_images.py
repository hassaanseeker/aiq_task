def insert_resized_image_data():
    """
    Function that inserts resized image data into sqlite database.
    """

    return f"INSERT INTO resized_image_data VALUES ({', '.join(['?'] * 151)});"
