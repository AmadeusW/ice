Developemnt log

## 2024-12-27
To get started, open 2 linux terminals

Device connector/simulator terminal
1. g++ -std=c++11 virtual_serial.cpp -pthread -o virtual_serial
1. ./virtual_serial

Dashboard terminal
1. venv/scripts/activate
1. pip install -r requirements.txt
1. python main.py

How about give it a better name, ICE - Interactive Control Engine

## 2024-12-16
Configuration file loader
Next up:
-[ ] Create the curses dashboard using that configuration, and hook up keyboard events


## 2024-12-15 curses dashboard
Created a curses dashboard that displays a sample state, and sends it to the device on each update
the device succesfully receives this information!

Next up: 
-[ ] make this extensible such that Dashboard loads _configuration_: user friendly name, serialization order, keyboard shortcut for toggling
-[ ] Hook up the received data to the real microcontroller code
-[ ] Replace all print with message handler, which redirects to curses if possible

## 2024-12-14 another approach
I decided to create two programs that communicate using serial port.
This will short cut us to Goal C, and allow for the other goals.
Under simulation mode, the microcontroller program will include 
C++ code which creates and communicates using a virtual serial port.
Under device telemetry mode, the microcontroller will use the real serial port.

Running:
- virtual_serial.cpp
  - `g++ -std=c++11 virtual_serial.cpp -pthread -o virtual_serial`
  - `./virtual_serial`
- main.py
  - `python main.py`
  - previous `main.py` is deleted

Next up: serialize the object which represents the game state on the microcontroller



## 2024-12-08 git init
Goal A: creating an application that can invoke C code and have a callback
Goal B: run the target microcontroller program through the application
Goal C: telemetry and control of the microcontroller program
Goal D: connect to actual microcontroller

Goal A met with Claude, 45m

