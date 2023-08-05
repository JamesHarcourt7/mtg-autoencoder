# get section of an image


import numpy as np
import matplotlib.pyplot as plt

# assume img is RGB
def get_section(img: np.ndarray):
    # get section of image

    bounding_box = [77, 38, 378, 450]
    section = img[bounding_box[0]:bounding_box[2], bounding_box[1]:bounding_box[3]]

    return section
