"""
This module downloads images from Internet
based on the query given by user
"""

import os
import shutil

from bing_image_downloader import downloader


def download_image(query, num, otpt_path):
    """
    Download images using Bing downloader package

    Args:
        query (str): User prompt
        num (int): number of images to download
        otpt_path: save images in the output directory
    """
    _ = downloader.download(query, limit=int(num), output_dir=otpt_path, adult_filter_off=True, force_replace=False,
                            timeout=60, verbose=True)
    return _


def delete_previous_images(folder):
    """

    Args:
        folder (str): path to delete old images

    Returns:
        None
    """
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    return
