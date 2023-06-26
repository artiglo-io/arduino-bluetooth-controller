# Description: Utility wrapper functions for tkinter
from tkinter import Button, StringVar, Label, Listbox, END
from bluetooth_utils import find_devices, connect_to_device, send_data, disconnect, receive_data

devices = []
connected_device = None
sock = None


def switch_button(button: Button, state=None):
    """
    Switch the state of a tkinter button
    :param state:
    :param button:
    :return:
    """
    if state is not None:
        button["state"] = state
    elif button["state"] == "normal":
        button["state"] = "disabled"
    else:
        button["state"] = "normal"
    button.update()


def switch_buttons(buttons: list, state=None):
    """
    Switch the state of a list of tkinter buttons
    :param state:
    :param buttons:
    :return:
    """
    for button in buttons:
        switch_button(button, state)


def switch_button_text(button: Button, text: str):
    """
    Switch the text of a tkinter button
    :param button:
    :param text:
    :return:
    """
    button["text"] = text


def find_blt(output, outputLabel, devices_list, connect_button,
             find_blt_button, control_buttons):
    """
    Tkinter command to find bluetooth devices

    :param control_buttons:
    :param find_blt_button:
    :param connect_button:
    :param devices_list:
    :param output:
    :type outputLabel:
    :return:
    """
    switch_button(find_blt_button, "disabled")
    switch_button(connect_button, "disabled")
    switch_buttons(control_buttons, "disabled")
    devices_list.delete(0, END)
    output.set("Looking for bluetooth devices...")
    outputLabel.update()

    global devices
    devices = find_devices()

    if len(devices) == 0:
        output.set("No bluetooth devices found")
        outputLabel.update()
        return
    else:
        output.set("Found " + str(len(devices)) + " bluetooth devices")
        outputLabel.update()
        for device in devices:
            devices_list.insert(END, device[1] + " - " + device[0])
        switch_button(connect_button, "normal")
        switch_button_text(connect_button, "Connect")
        switch_button(find_blt_button, "normal")


def handle_connect(device_pos: int, output: StringVar, outputLabel: Label, button: Button,
                   control_buttons):
    """
    Tkinter command to connect/disconnect to a bluetooth device
    :param control_buttons:
    :param button:
    :param device_pos:
    :param output:
    :param outputLabel:
    :return:
    """
    global connected_device
    global sock
    if button["text"] == "Disconnect":
        output.set(f"Disconnecting from  {connected_device}...")
        outputLabel.update()
        disconnect(sock)
        output.set(f"Disconnected from {connected_device}")
        outputLabel.update()
        switch_buttons(control_buttons, "disabled")
        switch_button_text(button, "Connect")
        return
    output.set(f"Connecting to {devices[device_pos][1]}...")
    outputLabel.update()
    try:
        switch_button(button, "disabled")
        sock = connect_to_device(devices[device_pos][0])
        connected_device = devices[device_pos][1]
    except OSError:
        output.set(f"Error connecting to {devices[device_pos][1]}, try using another device.")
        outputLabel.update()
        return
    except Exception as e:
        output.set(f"Unknown error: {e}")
        outputLabel.update()
        return
    finally:
        switch_button(button, "normal")

    output.set(f"Connected to {devices[device_pos][1]}")
    outputLabel.update()
    switch_buttons(control_buttons, "normal")
    switch_button_text(button, "Disconnect")


def send_message(data: str, output=None, outputLabel=None):
    """
    Tkinter command to send data to a bluetooth device
    :param outputLabel:
    :param output:
    :param data:
    :return:
    """
    global sock
    if sock is None:
        return

    try:
        send_data(sock, data)
    except Exception as e:
        if output is not None and outputLabel is not None:
            output.set(f"Unknown error: {e}")
            outputLabel.update()
