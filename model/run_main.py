"""
This module is the main file which calls all
other modules to create UI and prompt user for query,
run internet search to download image, and finally
run transformer model to generate caption
"""

import os
import logging

from model import *


def run_app(query, num_of_images):
    """
    Method that download images based on user prompted query from Bing API

    Args:
        query (str): User defined images query
        num_of_images (int): how many images to download

    Returns:
        str
    """
    old_image_path = os.getcwd() + "/model/output/dataset/"
    delete_previous_images(old_image_path)
    output_dir = os.getcwd() + "/model/output/dataset/"
    logger = logging.getLogger('[APP_IMG]')
    """If you want to use different logfile, instantiate new before this method using set_log_file method"""
    logger.info("==== DOWNLOADING IMAGES ===")
    try:
        _ = download_image(query, num_of_images, output_dir)
        old_directory = output_dir + query + "/"
        new_directory = output_dir + "Output" + "/"
        os.rename(old_directory, new_directory)
        return "## Download is completed, checkout 'Caption Images' tab"
    except Exception as e:
        return f"## Could not download images due to {e}"


def running_caption_generating_model():
    """
    Run the trained ML model to caption images

    Returns:
        list of tuple with images in PIL format and caption in str
    """
    images_directory = os.getcwd() + "/model/output/dataset/Output/"
    logger = logging.getLogger('[APP_IMG]')
    logger.info("==== CAPTIONING IMAGES===")
    captions = caption_images(images_directory)
    return captions
