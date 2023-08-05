import os
import numpy as np
import cv2
import section
import colours
import canny

if __name__ == '__main__':
    # get all images in directory
    directory = 'examples'

    # iterate through each image
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            print(filename)

            # read image
            img = cv2.imread(os.path.join(directory, filename))

            # convert to RGB
            img = np.array(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

            img_section = section.get_section(img)

            # calculate histogram
            hist = colours.histogram(img_section)

            # detect edges
            edges = canny.detect_edges(img_section)
