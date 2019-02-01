from Vector3 import *
from Ray import *
from Sphere import *
from Strike import *
from Roster import *
from Eye import *
from Picture import *
import math
import random

min = 0
max = 1000


def colour(ray, roster):
    strike = roster.hit(ray, min, max)
    if (strike):
        return (strike.normal + 1) / 2
    else:
        unitDirection = ray.direction.unit()
        t = (unitDirection.y + 1.0) / 2
        return  Vector3(1.0, 1.0, 1.0) * (1.0 - t) + Vector3(1.0, 0.5, 0.7) * t



width = 400
height = 200
samples = 2
eye = Eye()
pic = Picture(width, height)

roster = Roster()
roster.add(Sphere(Vector3(0.0, 0.0, -1.0), 0.5))
roster.add(Sphere(Vector3(0.0, -100.5, -1.0), 100.0))

for x in range(width):
    for y in range(height):
        col = Vector3()
        for s in range(samples):
            u = (x + random.random()) / float(width)
            v = (y + random.random()) / float(height)
            ray = eye.getRay(u, v)
            col += colour(ray, roster)
        col /= samples
        pic.pixel(x, y, col)

pic.ppm()
