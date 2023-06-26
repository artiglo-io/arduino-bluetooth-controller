# Description: This file contains functions to connect to a bluetooth device and send/receive data
from bluetooth import *


def find_devices() -> list:
    """
    Find all bluetooth devices in range
    :return devices:
    """
    devices = discover_devices(lookup_names=True)
    return devices


def connect_to_device(device: str) -> BluetoothSocket:
    """
    Connect to a bluetooth device
    :param device:
    :return sock:
    """
    sock = BluetoothSocket(RFCOMM)
    sock.connect((device, 1))
    return sock


def receive_data(sock: BluetoothSocket) -> str:
    """
    Receive data from a connected bluetooth device
    :param sock:
    :return data:
    """
    data = sock.recv(1024)
    return data.decode('UTF-8')


def disconnect(sock: BluetoothSocket):
    """
    Disconnect from a connected bluetooth device
    :param sock:
    :return:
    """
    sock.close()


def send_data(sock: BluetoothSocket, data: str):
    """
    Send data to a connected bluetooth device
    :param data:
    :param sock:
    """
    sock.send(data)


