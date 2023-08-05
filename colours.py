# get colour histogram of an image

import cv2
import numpy as np
import matplotlib.pyplot as plt

# assume img is RGB
def histogram(img: np.ndarray): 
    # calculate histogram
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    '''
    # plot histogram
    plt.figure()
    plt.title('Grayscale Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

    # plot all 3 channels
    plt.figure()
    plt.title('Colour Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')
    colors = ('r', 'g', 'b')
    for i, col in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])

    plt.show()
    '''

    return hist
