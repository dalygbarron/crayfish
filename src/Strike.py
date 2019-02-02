from Vector3 import *

class Strike:
    """Represents a ray hitting a medium at a given point and normal."""

    def __init__(self, medium, ray, distance, normal):
        self.medium = medium
        self.ray = ray
        self.distance = distance
        self.normal = normal

    def point(self):
        """gives the point of the strike"""
        return self.ray.point(self.distance)
