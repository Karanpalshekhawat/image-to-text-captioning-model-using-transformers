"""
This module reads input query
from the user
"""

import yaml
import pandas as pd


def read_query_and_img_count(path):
    """
    This function read input query for
    downloading images by the user

    Args:
        path (str):  path to read input query file from

    Returns:
        query (str): Search Query
        nms (int): Number of images to download
    """
    yml_file = path + "input_variables.yml"
    with open(yml_file) as file:
        df = pd.json_normalize(yaml.safe_load(file))
    return df.iloc[0]['query'], df.iloc[0]['Nums']
