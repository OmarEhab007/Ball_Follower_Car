# Ball Follower Car

This repo contains the code and instructions for building a ball follower car using a Raspberry Pi and a camera.

## Table of Contents

- [Overview](#overview)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Instructions](#instructions)

## Overview

The ball follower car is a Raspberry Pi-based robot that uses a camera to detect and follow a colored ball. The robot is built using a motor driver board, two DC motors, a battery pack, and a Raspberry Pi Camera Module. The robot is programmed in Python and uses OpenCV for image processing.

## Hardware Requirements

- Raspberry Pi (Model 3 or later)
- Raspberry Pi Camera Module
- L298N Dual H-Bridge Motor Driver Board
- Two DC Motors
- Ball Caster Wheel
- Battery Pack (6 AA batteries or 2 18650 batteries)
- Jumper Wires
- Breadboard
- Chassis and Wheels

## Software Requirements

- Raspbian OS
- Python 3
- OpenCV
- NumPy
- PiCamera

## Instructions

1. Connect the L298N motor driver board to the Raspberry Pi according to the pinout diagram provided in the repo.
2. Connect the DC motors to the motor driver board.
3. Mount the Raspberry Pi camera module on the chassis.
4. Connect the camera module to the Raspberry Pi.
5. Install Raspbian OS on the Raspberry Pi if it is not already installed.
6. Install the required software packages by running the following commands in the terminal:
