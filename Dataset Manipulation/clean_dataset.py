#!/usr/bin/python

import os

def check_txt_content(txt_content):
    for char in txt_content:
        if char.isdigit():
            return True
        return False

"""
Deletes all empty .txt files (annotations) in the given "txt_folder", 
when it detects an empty annotation file the function deletes also the 
corresponding .jpg image in the "images_folder"
"""
def delete_empty_files(txt_folder, images_folder):
    
    for filename in os.listdir(txt_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(txt_folder, filename)
            
            with open(file_path, 'r') as file:
                txt_content = file.read().strip()
                if check_txt_content(txt_content):  # Check if there's at least one digit in the .txt file
                    os.remove(file_path)
                    print(f"Deleted empty file: {file_path}")

                    # Construct the path to the corresponding .jpg image
                    data_name = os.path.splitext(filename)[0] 
                    image_path = os.path.join(images_folder, data_name + ".jpg")

                    if os.path.isfile(image_path):
                        os.remove(image_path)
                        print(f"Deleted corresponding image: {image_path}")

if __name__ == "__main__":
    txt_folder = "test/labels"
    images_folder = "test/images"

    delete_empty_files(txt_folder, images_folder)
    print("Finished.")
