# Autonomous Self-Driving Car 🚗

Educational Raspberry Pi 3 Model B+ + Arduino UNO autonomous-car reference project.

This project follows the general architecture described in the Udemy course **Build your Own Self Driving Car | Course 1 & Course 2**: Raspberry Pi master, Arduino slave, OpenCV image processing, lane following and track testing.

Course reference: https://www.udemy.com/course/selfdriving/

The code in this repository is original reference code and does not reproduce paid course source code.

## Hardware
- Raspberry Pi 3 Model B+
- Arduino UNO
- Raspberry Pi Camera Module
- L298N motor driver
- 4 DC geared motors
- 2 IR sensors
- HC-SR04-style ultrasonic sensor
- Robot chassis and wheels

## Software
Python 3, OpenCV, NumPy, PySerial, Arduino IDE.

## Architecture
Camera → Raspberry Pi → lane/signal processing → USB serial → Arduino UNO → L298N → motors.
IR and ultrasonic sensors provide track/safety information.

## Fixed wiring

### L298N → Arduino UNO
| L298N | Arduino |
|---|---:|
| ENA | D5 |
| IN1 | D7 |
| IN2 | D8 |
| ENB | D6 |
| IN3 | D9 |
| IN4 | D10 |

### Sensors → Arduino UNO
| Sensor | Arduino |
|---|---:|
| Left IR OUT | A0 |
| Right IR OUT | A1 |
| Ultrasonic TRIG | D11 |
| Ultrasonic ECHO | D12 |

### Raspberry Pi
- Camera → CSI connector
- Arduino → USB
- Serial baud → 115200

## Features
- Camera capture
- ROI lane processing
- Canny edge detection
- Hough-line lane estimation
- Proportional differential steering
- IR lane-end detection and U-turn
- Ultrasonic obstacle stop
- Basic traffic-light color detection
- Basic circular-sign detection
- Raspberry Pi ↔ Arduino serial control

## Run
```bash
sudo apt update
sudo apt install python3-opencv python3-numpy python3-serial
python3 code/raspberry_pi/main.py
```

## Safety
Educational prototype only. Test with wheels lifted first, use a physical power disconnect, and verify actual electrical ratings before operation. Do not power motors from the Raspberry Pi 5V rail.

## Author
Rushwanth S P
