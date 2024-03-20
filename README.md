# DexVisio

Computer Vision based based robotic arm.

## Table of Contents

- [Setup](#setup)
- [Description](#description)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Setup

### Prerequisites

- Arduino IDE
- Python 3.x
- OpenCV
- Mediapipe
- Servo library for Arduino

### Hardware Setup

1. Connect servos to your Arduino board(according to circuit diagram).
2. Upload the Arduino code (`Mimic_hand.ino`) to your Arduino board.

### Software Setup

1. Install Python dependencies:

   ```bash
   pip install opencv-python mediapipe pyserial
   ```

2. Run the Python script (`hand_control.py`).

## Description

The system captures live video from the webcam, detects hand gestures using Mediapipe, and sends corresponding signals to the connected Arduino board. The Arduino controls servos based on the received signals, enabling real-time control of devices using hand movements.

## Usage

1. Run the Python script (`hand_control.py`).
2. Perform hand gestures in front of the webcam.
3. The Arduino board will react to the recognized gestures by controlling the connected servos.

## Dependencies

- [OpenCV](https://opencv.org/): Open Source Computer Vision Library
- [Mediapipe](https://mediapipe.dev/): Framework for building multimodal (eg. video, audio, etc.) applied machine learning pipelines
- [PySerial](https://pypi.org/project/pyserial/): Python Serial Port Extension

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
