import cv2 as cv
import numpy as np

def rescue_camp_detection(img_path, segmented_image):
    detected_camps = []
    img = cv.imread(img_path)
    blur_img = cv.medianBlur(img, 3)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 7)
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 50, param1=50, param2=25, minRadius=0, maxRadius=0)

    circles = np.uint16(np.around(circles))
    for (x, y, r) in circles[0, :]:
        cv.circle(img, (x, y), r, (0, 255, 0), 3)

    color_map = {
        (255, 161, 230): "Pink Camp",
        (255, 186, 254): "Pink Camp",
        (255, 177, 253): "Pink Camp",
        (255, 176, 136): "Blue Camp",
        (255, 205, 171): "Blue Camp",
        (255, 221, 179): "Blue Camp",
        (218, 218, 221): "Grey Camp",
        (220, 220, 223): "Grey Camp"

    }


    for (x, y, r) in circles[0, :]:
        b, g, r = blur_img[y, x]
        center_color = (b, g, r)
        label = color_map.get(center_color, "Unknown")

        cv.putText(segmented_image, label, (x - 20, y - 40),
                   cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

        # ... inside your loop ...
        detected_camps.append({
            'color': label.replace(" Camp", ""),  # Clean the string to just "Pink", "Blue", etc.
            'loc': (x, y),
            'assigned': []  # Initialize empty list for assignments later
        })



        print(f"Detected {label} at center: {x}, {y} with color {center_color}" )

    return detected_camps , segmented_image






