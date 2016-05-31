
class Point:
    coords = None
    n = 0

    def __init__(self, coords):
        self.coords = coords
        self.n = len(coords) # Signifies the dimentions (for our case always 2 i.e. (X, Y))

    def __del__(self):
        return
