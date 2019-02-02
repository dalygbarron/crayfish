from Texture import *
from Vector3 import *
import math

class Checker(Texture):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def value(self, u, v, point):
        sines = math.sin(point.x * 10) * math.sin(point.y * 10) * math.sin(point.z * 10)
        if (sines > 0): return self.a
        return self.b
