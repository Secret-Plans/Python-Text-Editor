# Imports
import os
import sys

import colours
from document import doc


# Functions
def setup():
    enable_vt100()


def enable_vt100():
    if os.name == "nt":
        os.system("")


def clear_screen() -> None:
    sys.stdout.write("\033c")


def set_colour(colour : str = "gray") -> None:
    sys.stdout.write(f"\033[{colours.FORE[colour]}m")


def set_cursor_position(x : int = 1, y : int = 1) -> None:
    sys.stdout.write(f"\033[{y};{x}H")