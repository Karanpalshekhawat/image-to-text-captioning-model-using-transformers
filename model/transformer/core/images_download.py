"""
This module downloads images from Internet
based on the query given by user
"""

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
