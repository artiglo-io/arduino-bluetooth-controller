# Description

This is a simple program that allows you to control an Arduino via Bluetooth. It is designed to work with Arduino Motor
Shield Rev1.
It is written in Python 3.8 and uses pyBluez to communicate with the Arduino. It is compiled to an executable using
PyInstaller.

# Install pyBluez

Due to a bug in the latest version of pyBluez, we need to install it from the git repository.

```python -m pip install -e git+https://github.com/pybluez/pybluez.git#egg=pybluez```

# Compile

```pyinstaller arduino-bluetooth-controller.spec```