from Medium import *
from Vector3 import *
from Ray import *
from Strike import *

class Sphere(Medium):
    """A completely round medium for light to bounce off of."""
    def __init__(self, centre = Vector3(), radius = 1.0):
        self.centre = centre
        self.radius = radius

    def hit(self, ray, min, max):
        diff = ray.origin - self.centre
        a = ray.direction.dot(ray.direction)
        b = 2.0 * diff.dot(ray.direction)
        c = diff.dot(diff) - self.radius * self.radius
        discriminant = b * b - 4 * a * c
        if (discriminant > 0):
            distance = (-b - math.sqrt(b * b - a * c)) / a;
            if (distance < max and distance > min):
                return Strike(distance, (ray.point(distance) - self.centre) / self.radius)
            distance = (-b + math.sqrt(b * b - a * c)) / a;
            if (distance < max and distance > min):
                return Strike(distance, (ray.point(distance) - self.centre) / self.radius)
        return None
