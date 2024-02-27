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
    old_directory = output_dir + query + "/"
    new_directory = output_dir + "Output" + "/"
    os.rename(old_directory, new_directory)
    return "## Download is completed, checkout 'Caption Images' tab"


def running_caption_generating_model(num):
    images_directory = os.getcwd() + "/model/output/dataset/Output/"
    captions = caption_images(images_directory)
    return captions
