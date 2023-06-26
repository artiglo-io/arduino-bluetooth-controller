# Description: Utility functions for the application
import os
import sys


def load_icon(datafile: str) -> str:
    """
    Load an icon from the assets folder
    :param datafile:
    :return:
    """
    if not hasattr(sys, "frozen"):
        asset = os.path.join(os.path.dirname(__file__), datafile)
    else:
        asset = os.path.join(sys.prefix, datafile)
    return asset
