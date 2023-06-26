# Description: Main file of the project. It contains the GUI and the main loop of the program.
import os
from tkinter import *
import keyboard

from settings import ICON_PATH_WIN, APPLICATION_NAME, APPLICATION_VERSION, WINDOW_RESIZEABLE, \
    ICON_PATH_LINUX
from tkinter_utils import find_blt, handle_connect, send_message
from utils import load_icon

root = Tk()
root.title(f"{APPLICATION_NAME} - {APPLICATION_VERSION}")
root.resizable(WINDOW_RESIZEABLE, WINDOW_RESIZEABLE)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

if "posix" == os.name:
    datafile = load_icon(ICON_PATH_LINUX)
    icon = PhotoImage(file=datafile)
    root.iconphoto(False, icon)
else:
    datafile = load_icon(ICON_PATH_WIN)
    root.iconbitmap(datafile)

find_bluetooth_devices_button = Button(root, text="Find Bluetooth Devices")
find_bluetooth_devices_button.configure(
    command=lambda: find_blt(output, outputLabel, devices_list, connect_button, find_bluetooth_devices_button,
                             control_buttons))
find_bluetooth_devices_button.grid(row=1, column=0, sticky="ew", columnspan=3, padx=10, pady=(10, 0))

devices_list = Listbox(root, selectmode=SINGLE, width=40, height=10, borderwidth=1, relief="solid")
devices_list.grid(row=2, column=0, padx=10, pady=10, sticky="ew", columnspan=3)

connect_button = Button(root, text="Connect")
connect_button.configure(
    command=lambda: handle_connect(devices_list.curselection()[0], output, outputLabel, connect_button,
                                   control_buttons),
    state="disabled")
connect_button.grid(row=3, column=0, sticky="ew", padx=10, pady=(0, 10), columnspan=3)

top_button = Button(root, text="Forward", command=lambda: send_message("1", output, outputLabel), state="disabled",
                    width=10, height=1, repeatdelay=100, repeatinterval=100)
top_button.grid(row=4, column=1,  padx=5, pady=5, sticky="ew")

left_button = Button(root, text="Left", command=lambda: send_message("2", output, outputLabel), state="disabled",
                     width=10, height=1, repeatdelay=100, repeatinterval=100)
left_button.grid(row=5, column=0, padx=(10, 5), pady=5, sticky="ew")

stop_button = Button(root, text="Stop", command=lambda: send_message("3", output, outputLabel), state="disabled",
                     width=10, height=1, repeatdelay=100, repeatinterval=100)
stop_button.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

right_button = Button(root, text="Right", command=lambda: send_message("4", output, outputLabel), state="disabled",
                      width=10, height=1, repeatdelay=100, repeatinterval=100)
right_button.grid(row=5, column=2, padx=(5, 10), pady=5, sticky="ew")

bottom_button = Button(root, text="Backward", command=lambda: send_message("5", output, outputLabel), state="disabled",
                       width=10, height=1, repeatdelay=100, repeatinterval=100)
bottom_button.grid(row=6, column=1, padx=5, pady=5, sticky="ew")

keyboard_info = Label(root, text="Use WASD and space to control the car.", width=40, height=1, borderwidth=1,
                      relief="solid",
                      )
output = StringVar()

outputLabel = Label(root, textvariable=output, background="white", width=40, height=3, borderwidth=1, relief="solid",
                    wraplength=250)
outputLabel.grid(row=7, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=3)

keyboard_info.grid(row=8, column=0, padx=10, pady=(0, 10), sticky="ew", columnspan=3)
control_buttons = [top_button, left_button, stop_button, right_button, bottom_button]
root.bind("<KeyPress>", lambda e: keyboard.handle_key(e))

root.mainloop()
