"""
This module is the main file which calls all
other modules to create UI and prompt user for query,
run internet search to download image, and finally
run transformer model to generate caption
"""

import os

from model import *


def run_app(query, num_of_images):
    old_image_path = os.getcwd() + "/model/output/dataset/"
    delete_previous_images(old_image_path)
    output_dir = os.getcwd() + "/model/output/dataset/"
    _ = download_image(query, num_of_images, output_dir)
    images_directory = output_dir + query + "/"
    captions = caption_images(images_directory)
    images_list = list(captions.keys())
    label_list = list(captions.values())
    pil_img = convert_jpg_images_to_pil(list(captions.keys())[0])
    return pil_img
