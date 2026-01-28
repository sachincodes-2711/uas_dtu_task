import cv2
import cv2 as cv
import numpy as np
import os

def casualties_detection(img_path, step_2_img):
    img = cv.imread(img_path)
    detected_casualties = []

    if img is None:
        return
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    _, thresh = cv.threshold(gray, 160, 255, cv.THRESH_BINARY)

    contours, _ = cv.findContours(
        thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
    )

    filtered_contours = []
    for cnt in contours:
        if cv.contourArea(cnt) < 400:
            filtered_contours.append(cnt)

    for cnt in filtered_contours:
        peri = cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt, 0.04 * peri, True)
        corners = len(approx)

        M = cv.moments(cnt)
        if M["m00"] == 0:
            continue

        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        (x, y), radius = cv.minEnclosingCircle(cnt)
        cX, cY = int(x), int(y)

        if corners == 3:
            shape = "Elder"
        elif corners == 4:
            shape = "Adult"
        elif corners in [8, 10, 12]:
            shape = "Child"
        else:
            shape = "Unknown"

        b , g , r = img[cY, cX]
        center_color = (b,g,r)
        color_map = {
            (117, 246, 193): "Safe",
            (115,245,191): "Safe",
            (114,244,190): "Safe",
            (89, 218, 255): "Mild",
            (79,216,255): "Mild",
            (159,167,255): "Severe",
            (177, 186, 255): "Severe",
            (187, 197, 255): "Severe"
            }
        label = color_map.get(center_color, "Unknown")

        detected_casualties.append({
            'loc': (cX, cY),
            'type': shape,
            'severity': label
        })

        print(f"Found {shape} at ({cX}, {cY}) with {label}  and {center_color}")

        cv.putText(
            step_2_img,
            f"{shape},{label}",
            (cX - 20, cY - 20),
            cv.FONT_HERSHEY_SIMPLEX,
            0.4,
            (0, 0, 0),
            1
        )

    cv.drawContours(step_2_img, filtered_contours, -1, (0, 0, 0), 1)



    return detected_casualties, step_2_img





