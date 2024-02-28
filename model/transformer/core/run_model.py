"""
This module downloads already trained hugging face model
and use that to caption images.

Later on, will replace this functionality with self trained model
"""

import glob

from transformers import pipeline, VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image


def caption_images(path):
    """
    This function calls NLP connect model of hugging face
    and uses it to generate caption for an image.

    Args:
        path (str): directory to read images

    Returns:
        captions (dict): dictionary with image information
                         and its generated captions
    """
    img_and_captions = []
    image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

    img_list = glob.glob(path + "*.jpg")
    for img in img_list:
        opn_image = Image.open(img)
        caption = image_to_text(opn_image)[0]['generated_text']
        img_and_captions.append((opn_image, caption))

    return img_and_captions


def convert_jpg_images_to_pil(img_ls):
    """
    Convert images from jpg to Python Image Library (PIL) format
    Args:
        img_ls: list of jpg images

    Returns:
        list of pil images
    """

    pil_image = []
    for img in img_ls:
        pil_image.append(Image.open(img))
    return pil_image
