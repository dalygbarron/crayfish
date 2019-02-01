from Ray import *

class Eye:
    def __init__(self):
        self.topLeft = Vector3(-2.0, 1.0, -1.0)
        self.horizontal = Vector3(4.0)
        self.vertical = Vector3(0.0, -2.0)
        self.origin = Vector3()

    def getRay(self, u, v):
        return Ray(self.origin, self.topLeft + self.horizontal * u + self.vertical * v - self.origin)
