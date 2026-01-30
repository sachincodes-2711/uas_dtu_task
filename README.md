# Search and Rescue UAV Image Processing System

## UAS-DTU Round 2 – Software Department

This repository contains a Python-based computer vision system developed for the **UAS-DTU Round 2 Technical Task**. The project focuses on autonomous image segmentation, feature detection, and optimal decision-making for **Search and Rescue operations** using UAV imagery.

---

## Problem Statement

Given aerial images captured after a shipwreck:

* Segment **land** and **ocean** regions
* Detect **rescue camps** with fixed capacities
* Detect and classify **casualties** based on:

  * Age group (Child, Elder, Adult)
  * Medical severity (Severe, Mild, Safe)
* Assign each casualty to the **best possible rescue camp** while:

  * Respecting camp capacity
  * Maximizing overall rescue priority

---

## System Overview

The complete processing pipeline is:

1. Land–Ocean Segmentation
2. Rescue Camp Detection
3. Casualty Detection and Classification
4. Priority Score Computation
5. Optimal Camp Assignment
6. Final Visualization and Console Output

All steps are fully automated and executed through a single entry point.

---

## Project Structure

```
project/
│
├── main.py
├── image_ocean_segmentation.py
├── rescue_camp_detection.py
├── casualties_detection.py
├── casualties_assignment.py
├── images/
│   ├── 1.png
│   ├── 2.png
│   └── ...
```

---

## Module Description

### 1. image_ocean_segmentation.py

* Separates land and ocean using BGR color thresholding
* Applies bilateral filtering for noise reduction
* Overlays:

  * Yellow on land regions
  * Cyan on ocean regions

---

### 2. rescue_camp_detection.py

* Detects circular rescue camps using Hough Circle Transform
* Identifies camp type (Pink, Blue, Grey) via center pixel color
* Initializes camp data structures with capacity constraints

---

### 3. casualties_detection.py

* Detects casualties using contour detection
* Classifies age group using geometric shape approximation
* Classifies medical severity using center color sampling
* Annotates detected casualties on the image

---

### 4. casualties_assignment.py

* Computes priority score for each casualty
* Sorts casualties by priority and severity
* Assigns each casualty to the nearest available rescue camp
* Draws arrows indicating final assignments
* Computes total camp priority and rescue ratio

---

### 5. main.py

* Acts as the pipeline controller
* Executes all processing stages sequentially
* Displays final annotated image
* Supports batch processing of multiple images

---

## Priority Model

### Age Group Priority

| Age Group | Score |
| --------- | ----- |
| Child     | 3     |
| Elder     | 2     |
| Adult     | 1     |

### Medical Severity Priority

| Severity | Score |
| -------- | ----- |
| Severe   | 3     |
| Mild     | 2     |
| Safe     | 1     |

### Final Priority

```
Priority Score = Age Priority × Medical Severity Priority
```

---

## Rescue Camp Capacities

| Camp | Capacity |
| ---- | -------- |
| Pink | 3        |
| Blue | 4        |
| Grey | 2        |

---

## Requirements

### Software

* Python 3.8 or higher
* OpenCV 4.x
* NumPy

### Supported Operating Systems

* Ubuntu 20.04+
* Windows 10 / 11

---

## Installation

### Linux (Ubuntu)

```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install opencv-python numpy
```

### Windows

1. Install Python 3.10+
2. Install dependencies:

```cmd
pip install opencv-python numpy
```

---

## Execution

Place all `.png` input images in the project directory and run:

```bash
python main.py
```

The system will display processed images and print structured results to the console.

---

## Output

* Segmented land–ocean image
* Labeled rescue camps
* Labeled casualties
* Arrows showing casualty-to-camp assignments
* Camp-wise priority totals
* Rescue ratio (Pr)

---

## Notes

* Designed for digitally generated UAV images with consistent color coding
* Distance calculations are pixel-based (Euclidean)
* Capacity constraints are strictly enforced

---

## Author

Sachin Chaudhary

---

## License

This project is intended for academic and recruitment evaluation purposes only.
