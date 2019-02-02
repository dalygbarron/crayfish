from Medium import *
from Vector3 import *
from Ray import *
from Strike import *

class Sphere(Medium):
    """A completely round medium for light to bounce off of."""
    def __init__(self, material, centre = Vector3(), radius = 1.0):
        Medium.__init__(self, material)
        self.centre = centre
        self.radius = radius

    def hit(self, ray, min, max):
        diff = ray.origin - self.centre
        a = ray.direction.dot(ray.direction)
        b = diff.dot(ray.direction)
        c = diff.dot(diff) - self.radius * self.radius
        discriminant = b * b - a * c
        if (discriminant > 0):
            distance = (-b - math.sqrt(b * b - a * c)) / a;
            if (distance < max and distance > min):
                return Strike(self, ray, distance, (ray.point(distance) - self.centre) / self.radius)
            distance = (-b + math.sqrt(b * b - a * c)) / a;
            if (distance < max and distance > min):
                return Strike(self, ray, distance, (ray.point(distance) - self.centre) / self.radius)
        return None
