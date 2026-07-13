#!/usr/bin/env python3

import os
import requests

# Replace with your external IP address
url = "http://<external-IP-address>/fruits/"

# Directory containing the text files
description_dir = os.path.expanduser("~/supplier-data/descriptions")

# Process each text file
for filename in os.listdir(description_dir):

    if filename.endswith(".txt"):

        file_path = os.path.join(description_dir, filename)

        with open(file_path, "r") as file:
            lines = file.read().splitlines()

        # Create JSON dictionary
        fruit = {
            "name": lines[0],
            "weight": int(lines[1].replace(" lbs", "")),
            "description": lines[2],
            "image_name": os.path.splitext(filename)[0] + ".jpeg"
        }

        # Upload data
        response = requests.post(url, json=fruit)

        if response.status_code == 201:
            print(f"Successfully uploaded {fruit['name']}")
        else:
            print(f"Failed to upload {fruit['name']}")
            print(f"Status Code: {response.status_code}")
            print(response.text)
