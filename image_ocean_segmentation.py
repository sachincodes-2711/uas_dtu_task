import numpy as np
import cv2 as cv
import os

def land_ocean_segmentation(img_path):
    img = cv.imread(img_path)
    img_blur = cv.bilateralFilter(img,20,25,75)
    #d = increase for noise reduction
    #sigma_color = Small value (e.g., 10–50): Only pixels with very similar colors will blur together. This keeps edges extremely sharp.
    #simga_space = Large value: Distant pixels (within the diameter $d$) will have more influence on the result.



    lower_limit_green = np.array([25, 120, 25])
    upper_limit_green = np.array([50,160, 50])

    lower_limit_blue = np.array([90,50,20])
    upper_limit_blue = np.array([150,80, 50])

    mask_1 = cv.inRange(img_blur, lower_limit_green, upper_limit_green)
    mask_2 = cv.inRange(img_blur, lower_limit_blue, upper_limit_blue)
    img[mask_1 > 0 ] = [0,255,255]
    img[mask_2 > 0 ] = [255,255,0]

    return img


