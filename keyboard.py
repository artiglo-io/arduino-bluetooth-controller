# Description: This file contains the keyboard input handling code
from tkinter_utils import send_message

lastKeyPressTime = 0
# Delay between key presses in milliseconds
delay = 100


def handle_key(e):
    """
    Handle the keyboard input
    :param e:
    :return:
    """
    global lastKeyPressTime
    current_time = e.time
    if lastKeyPressTime == 0 or current_time - lastKeyPressTime >= delay:
        lastKeyPressTime = current_time
        if e.char == "w":
            send_message("1")
        elif e.char == "a":
            send_message("2")
        elif e.char == " ":
            send_message("3")
        elif e.char == "d":
            send_message("4")
        elif e.char == "s":
            send_message("5")
