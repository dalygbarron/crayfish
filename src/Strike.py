from Vector3 import *

class Strike:
    """Represents a ray hitting a medium at a given point and normal."""
    def __init__(self, distance = 0.0, normal = Vector3()):
        self.distance = distance
        self.normal = normal
