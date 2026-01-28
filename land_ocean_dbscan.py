import numpy as np
import cv2 as cv


def land_ocean_segmentation_hsv(img_path):
    img = cv.imread(img_path)
    if img is None: return

    # 1. Bilateral Filter is great, but Median Blur is faster for removing icons
    # We use a slight blur to smooth out the grain in the blue/green areas
    img_blur = cv.bilateralFilter(img, 9, 75, 75)

    # 2. Convert to HSV
    hsv = cv.cvtColor(img_blur, cv.COLOR_BGR2HSV)

    # 3. Define HSV ranges
    # Hue: 0-180 (Green is roughly 35-85, Blue is roughly 90-130)
    # Saturation: 0-255 (Strength of color)
    # Value: 0-255 (Brightness)

    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])

    lower_blue = np.array([90, 40, 40])
    upper_blue = np.array([135, 255, 255])

    # 4. Create Masks
    mask_land = cv.inRange(hsv, lower_green, upper_green)
    mask_ocean = cv.inRange(hsv, lower_blue, upper_blue)

    result = img.copy()
    result[mask_land > 0] = [0, 255, 255]  # Neon Yellow/Green
    result[mask_ocean > 0] = [255, 255, 0]  # Cyan

    cv.imshow('Original', img)
    cv.imshow('Optimized Segmentation', result)
    cv.waitKey(0)
    cv.destroyAllWindows()


land_ocean_segmentation_hsv('1.png')