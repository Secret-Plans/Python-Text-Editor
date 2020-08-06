# Imports
from msvcrt import getch

import render
from document import Doc
from editor import Editor
from keydata import Keydata


# Functions
def getkey() -> Keydata:
    key_ch = getch()
    if key_ch == b"\xe0":
        return Keydata(getch().decode(), True)
    return Keydata(key_ch.decode())


# Main
def main():
    render.setup()
    editor = Editor()


if __name__ == "__main__":
    main()