# Imports
from msvcrt import getch

import render
from document import doc


# Functions
def getkey():
    key = getch()
    if key == b"\xe0":
        return getch()
    return key


# Main
def main():
    render.setup()


if __name__ == "__main__":
    main()