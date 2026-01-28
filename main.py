import cv2
import cv2 as cv
import numpy as np
import os
import casualties_detection as casualties_detection
import rescue_camp_detection as rescue_camp_detection
import image_ocean_segmentation as image_ocean_segmentation
import casualties_assignment as casualties_assignment

def final_run(img_path):
    segmented_image = image_ocean_segmentation.land_ocean_segmentation(img_path)
    detected_camps , step_2_img = rescue_camp_detection.rescue_camp_detection(img_path, segmented_image)
    detected_casualties , step_3_img = casualties_detection.casualties_detection(img_path, step_2_img)
    step3img = step_3_img.copy()
    camps, step_4_img = casualties_assignment.assign_casualties(detected_casualties, detected_camps, step_3_img)

    return camps, step_4_img

camps, step_4_img = final_run("8.png")
cv.imshow("Camps", step_4_img)
print(camps)
cv.waitKey(0)
cv.destroyAllWindows()

for img_path in os.listdir("./"):
    if img_path.endswith(".png"):
        final_run(img_path)
        cv.imshow(f"camps{img_path}", step_4_img)
        cv.waitKey(0)
        cv.destroyAllWindows()

q