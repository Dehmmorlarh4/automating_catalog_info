#!/usr/bin/env python3

import os
from PIL import Image

# Directory containing the images
source_dir = os.path.expanduser("~/supplier-data/images")

# Process each file in the directory
for filename in os.listdir(source_dir):

    # Process only TIFF images
    if filename.lower().endswith(".tiff"):
        input_path = os.path.join(source_dir, filename)

        # Create output filename with .jpeg extension
        output_filename = os.path.splitext(filename)[0] + ".jpeg"
        output_path = os.path.join(source_dir, output_filename)

        try:
            with Image.open(input_path) as img:
                # Convert to RGB (required for JPEG)
                img = img.convert("RGB")

                # Resize image
                img = img.resize((600, 400))

                # Save as JPEG
                img.save(output_path, "JPEG")

                print(f"Processed: {output_filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")
