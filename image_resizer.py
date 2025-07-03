import os
from PIL import Image

# Input and Output folder paths
input_folder = "input_images"
output_folder = "resized_images"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Set your Custom size
new_size = (300, 300)      # Width x Height in pixels

for filename in os.listdir(input_folder):  #Gets all files in the input folder
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  
        try:
            img_path = os.path.join  #Combines the input folder path with the filename(input_folder, filename)
            img = Image.open(img_path)  # Opens the image file  

            # Resize and convert to PNG
            img_resized = img.resize(new_size)
            new_filename = os.path.splitext(filename)[0] + ".png"
            img_resized.save(os.path.join(output_folder, new_filename), "PNG")

            print(f"Processed: {filename} -> {new_filename}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
