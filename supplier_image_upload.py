#!/usr/bin/env python3
import os
import requests

# Directory containing the processed JPEG images
image_dir = os.path.expanduser("~/supplier-data/images")

# URL for image upload
url = "http://localhost/upload/"

# Iterate through all files in the directory
for filename in os.listdir(image_dir):

    # Upload only JPEG images
    if filename.lower().endswith(".jpeg"):
        image_path = os.path.join(image_dir, filename)

        with open(image_path, "rb") as image_file:
            files = {"file": image_file}

            response = requests.post(url, files=files)

            if response.status_code == 201:
                print(f"Uploaded: {filename}")
            else:
                print(f"Failed to upload {filename}")
                print(f"Status Code: {response.status_code}")
