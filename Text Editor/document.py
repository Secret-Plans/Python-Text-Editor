# Imports


# Class
class Doc:
    lines : list = []


    # Methods
    def __init__(self):
        pass
    

    def load_doc(self, path : str):
        with open(path, "r") as f:
            self.lines = f.read().split("\n")