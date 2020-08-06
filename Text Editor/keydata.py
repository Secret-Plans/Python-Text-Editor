# Imports


# Class
class Keydata:
    keycode : str


    def __init__(self, keycode : str, special : bool = False):
        if special:
            keycode = self.evaluate_special_keycode(keycode)
        self.keycode = keycode
    

    def evaluate_special_keycode(self, keycode : str) -> str:
        """Gets a more readable string representation of special keycodes from the keyboard.

        Special keycodes are as follows:

        R : insert
        S : delete
        G : home
        O : end
        I : page up
        Q : page down

        H : arrow up
        K : arrow left
        M : arrow right
        P : arrow down

        \r   : enter/return
        \x08 : backspace
        \x1b : esc

        Args:
            keycode (str): The keycode to be evaluated.

        Returns:
            str: A more readable representation of the key.
        """
        
        special_keycodes = {
            "R": "ins",
            "S": "del",
            "G": "home",
            "O": "end",
            "I": "pg up",
            "Q": "pg dn",
            
            "H": "dir up",
            "K": "dir lt",
            "M": "dir rt",
            "P": "dir dn",

            "\r": "rtn",
            "\x08": "bck",
            "\x1b": "esc"
        }
        try:
            return special_keycodes[keycode]
        except KeyError:
            return "[?]"