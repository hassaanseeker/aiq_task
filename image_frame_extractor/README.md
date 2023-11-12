# Image Frame Extractor

This application extracts image frames based on depth values. Follow the steps below to set up and run the application.

## Setup

1. Run the following command from inside the `image_frame_extractor` folder to create the image table:

   ```bash
   python3 repositories/create_image_table.py
  ```
2. Next we need to run the command from inside the image_frame_extractor folder:

    ```bash
    python3 main.py
    ```
3. Then copy the aiq_image_task.db to flask_image_application folder.


4. Next run docker commands as below:
    ```bash
    docker build -t image_frame_extractor. 
    docker run -p 4000:8080 image_frame_extractor
    ```
5. Goto http://localhost:4000 and play with the image extractor application:

<img width="492" alt="image" src="https://github.com/hassaanseeker/aiq_task/assets/7199288/ab269705-fcf9-492c-833e-18cfda090379">
