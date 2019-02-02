from Vector3 import *

class Bounce:
    """Represents a ray bouncing off a medium's material and getting modified by it."""

    def __init__(self, attenuation = Vector3(), scatter = None):
        self.attenuation = attenuation
        self.scatter = scatter
