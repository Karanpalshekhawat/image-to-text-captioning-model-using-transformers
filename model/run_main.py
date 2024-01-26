"""
This module is the main file which calls all
other modules to create UI and prompt user for query,
run internet search to download image, and finally
run transformer model to generate caption
"""

import os

from model import *

if __name__ == "__main__":
    old_image_path = os.getcwd() + "/model/output/dataset/"
    delete_previous_images(old_image_path)
    path = os.getcwd() + "/model/static_data/"
    query, nums = read_query_and_img_count(path)
    output_dir = os.getcwd() + "/model/output/dataset/"
    _ = download_image(query, nums, output_dir)
    images_directory = output_dir + query + "/"
    captions = caption_images(images_directory)
