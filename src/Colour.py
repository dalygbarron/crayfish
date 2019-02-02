from Texture import *

class Colour(Texture):
    def __init__(self, col):
        self.col = col

    def value(self, u, v, point):
        return self.col
