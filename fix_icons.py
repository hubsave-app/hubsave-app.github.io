import os
from PIL import Image

mipmap_folders = ["mipmap-mdpi", "mipmap-hdpi", "mipmap-xhdpi", "mipmap-xxhdpi", "mipmap-xxxhdpi"]
base_dir = "app/src/main/res"

for folder in mipmap_folders:
    folder_path = os.path.join(base_dir, folder)
    if not os.path.exists(folder_path): continue
    
    for filename in ["ic_launcher.png", "ic_launcher_round.png"]:
        file_path = os.path.join(folder_path, filename)
        if os.path.exists(file_path):
            try:
                # Open the image (which might be a JPEG internally)
                img = Image.open(file_path)
                # Convert to RGB (in case it has an alpha channel or is CMYK, though unlikely for JPEG)
                img = img.convert("RGBA")
                # Save as a true PNG
                temp_path = file_path + ".temp.png"
                img.save(temp_path, "PNG")
                
                # Replace original file
                os.replace(temp_path, file_path)
                print(f"Converted {file_path} to true PNG.")
            except Exception as e:
                print(f"Error converting {file_path}: {e}")
