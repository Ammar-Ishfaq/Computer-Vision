# YOLOv3 Object Detection

This project implements YOLOv3 (You Only Look Once, Version 3) for object detection and counting in Python. YOLOv3 is a state-of-the-art, real-time object detection system. This repository provides the code to run YOLOv3 using the pre-trained weights, enabling you to detect and count objects in images and videos.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the GUI](#running-the-gui)
  - [Using the USB Camera](#using-the-usb-camera)
- [Model Download](#model-download)
- [Dependencies](#dependencies)
- [Recommendations](#recommendations)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Introduction

YOLOv3 is a popular object detection model known for its speed and accuracy. This project provides a simple and efficient implementation of YOLOv3 in Python, allowing you to perform object detection tasks with ease.

## Features

- Real-time object detection and counting
- Supports detection in images and videos
- Easy-to-use graphical user interface (GUI)
- Pre-trained YOLOv3 weights
- USB camera support
- Tested on M1 Pro Apple Silicon, runs smoothly

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/yolov3-object-detection.git
    cd yolov3-object-detection
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Download the YOLOv3 weights:

    You can download the pre-trained YOLOv3 weights from one of the following links and save it in the `weights` directory:

    - [YOLOv3 Weights (official)](https://pjreddie.com/media/files/yolov3.weights)
    - [YOLOv3 Weights (MEGA)](https://mega.nz/file/RY9iULqY#LnaES0xxcfUDTSwcjJ3xyrDpl0Q_r_yzBBVcaPlwCBQ)

## Usage

### Running the GUI

To run this project, execute `Gui_Image_Detection.py`. The GUI allows you to select an image or video for object detection and counting. You can also choose to use a USB camera by updating the camera number mentioned in the file.

1. Run the GUI script:

    ```bash
    python Gui_Image_Detection.py
    ```

2. In the GUI, select whether you want to detect objects in an image or a video.
3. Follow the prompts to select the image or video file.
4. If using a USB camera, make sure to update the camera number in the script.

### Using the USB Camera

1. Connect your USB camera.
2. Update the camera number in the script `Gui_Image_Detection.py`.
3. Run the GUI script:

    ```bash
    python Gui_Image_Detection.py
    ```

## Model Download

Download the pre-trained YOLOv3 weights from one of the following links and save it in the `weights` directory:

- [YOLOv3 Weights (official)](https://pjreddie.com/media/files/yolov3.weights)
- [YOLOv3 Weights (MEGA)](https://mega.nz/file/RY9iULqY#LnaES0xxcfUDTSwcjJ3xyrDpl0Q_r_yzBBVcaPlwCBQ)

## Dependencies

- Python 3.7+
- OpenCV
- NumPy
- Pillow

You can install all dependencies using:

```bash
pip install -r requirements.txt
