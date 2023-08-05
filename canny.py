# canny edge detection

import cv2
import numpy as np
import matplotlib.pyplot as plt

# assume img is RGB
def detect_edges(img: np.ndarray):
    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # blur image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # detect edges
    canny = cv2.Canny(blur, 50, 150)

    '''
    # plot images
    plt.figure()
    plt.imshow(canny, cmap='gray')
    plt.show()
    '''

    return canny