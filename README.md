# Description

This is a simple program that allows you to control an Arduino via Bluetooth. It is designed to work with Arduino Motor
Shield Rev1.
It is written in Python 3.8 and uses pyBluez to communicate with the Arduino. It is compiled to an executable using
PyInstaller.

# UI Design
![ui-windows](./docs/assets/ui-windows.png?raw=true "Title")

UI design may be different on other platforms.

# Arduino Setup
Sample code for Arduino is in the `docs/code/arduino` directory. It is written in C++ (Arduino) and uses the Arduino Motor Shield Rev1.

# Install pyBluez

Due to a bug in the latest version of pyBluez, we need to install it from the git repository.

```python -m pip install -e git+https://github.com/pybluez/pybluez.git#egg=pybluez```

# Compile

```pyinstaller arduino-bluetooth-controller.spec```