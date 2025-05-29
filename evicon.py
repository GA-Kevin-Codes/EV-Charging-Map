import os
from PIL import Image

# Set folder and target size
input_folder = "/home/kevin/EV-map"
output_folder = input_folder
target_size = (100, 100)  # Width x Height

# Make output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all PNG files
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
            resized = img.resize(target_size, Image.LANCZOS)
            save_path = os.path.join(output_folder, filename)
            resized.save(save_path)
            print(f"Resized and saved: {save_path}")
