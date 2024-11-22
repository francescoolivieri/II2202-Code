#!/usr/bin/python

import cv2
import numpy as np
import random as rand
import os

"""
This function add light disturbance to all the images in the folder "images_folder".
If "image_visualization" is True, the program will show each modified image.
"""
def modify_images(images_folder, image_visualization):
    
    for image_name in os.listdir(images_folder):
        image = cv2.imread(os.path.join("images", image_name))

        width = image.shape[1] 
        height = image.shape[0]

        # Create an additional layer (same size as the image)
        light_disturbance_layer = np.zeros((height, width, 3), dtype=np.uint8)

        light_source_center = (int(width * rand.uniform(0, 1.0)), int(height * rand.uniform(0, 0.2)))  # Position it randomly at the top of the image
        light_source_radius = min(width, height) // 12

        # Draw the light source
        cv2.circle(light_disturbance_layer, light_source_center, light_source_radius, (255, 255, 255), -1)

        # Generate rays from the light source, like a sun
        num_rays = 50  
        ray_length = min(width, height)

        # Draw each ray
        for i in range(num_rays):
            angle = np.random.uniform(0, 2 * np.pi) # Random angle
            
            start_point = light_source_center
            end_point = (int(light_source_center[0] + ray_length * np.cos(angle)), int(light_source_center[1] + ray_length * np.sin(angle)))
            
            thickness = np.random.randint(2, 5)
            cv2.line(light_disturbance_layer, start_point, end_point, (255, 255, 255), thickness)

        # Apply Gaussian blur to soften the rays
        light_disturbance_layer = cv2.GaussianBlur(light_disturbance_layer, (101, 101), 0)

        # Blend the light disturbance layer with the original image
        blended = cv2.addWeighted(image, 1, light_disturbance_layer, 0.4, 0)  # Stronger blending

        alpha = 1.1  # Contrast control (1.0-3.0)
        beta = 50    # Brightness control (0-100)

        # Apply contrast and brightness
        adjusted = cv2.convertScaleAbs(blended, alpha=alpha, beta=beta)

        # Save the resulting image
        folder_path = f"output_images_alpha{alpha}_beta{beta}"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        cv2.imwrite(os.path.join(folder_path, image_name), adjusted)
        
        if(image_visualization):
            cv2.imshow('Modified Image', adjusted)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


if __name__ == "__main__":
    images_folder = "input_images" # PATH to images folder
    image_visualization = False # if True show every image modified

    modify_images(images_folder, image_visualization)
    print("Finished.")

