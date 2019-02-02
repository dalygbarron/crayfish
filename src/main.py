from Vector3 import *
from Ray import *
from Sphere import *
from Strike import *
from Roster import *
from Eye import *
from Lambert import *
from Metal import *
from Picture import *
import math
import random

min = 0.001
max = 10000000
bounceDepth = 50




def colour(ray, roster, depth = 0):
    strike = roster.hit(ray, min, max)
    if (strike):
        bounce = strike.medium.material.scatter(strike)
        if (depth >= bounceDepth or not bounce.scatter): return Vector3()
        return colour(bounce.scatter, roster, depth + 1) * bounce.attenuation
    else:
        unitDirection = ray.direction.unit()
        t = (unitDirection.y + 1.0) / 2
        return  Vector3(1.0, 1.0, 1.0) * (1.0 - t) + Vector3(0.5, 0.7, 1.0) * t



width = 512
height = 256
samples = 2
eye = Eye()
pic = Picture(width, height)

roster = Roster()
brick = Lambert(Vector3(0.5, 0.5, 0.5))
grass = Lambert(Vector3(0.8, 0.8, 0))
mirror = Metal(Vector3(0.8, 0.65, 0.5))

roster.add(Sphere(brick, Vector3(0.0, 0.0, -1.0), 0.5))
roster.add(Sphere(grass, Vector3(0.0, -100.5, -1.0), 100.0))
roster.add(Sphere(mirror, Vector3(1.0, 0.0, -1.0), 0.5))
roster.add(Sphere(mirror, Vector3(-1.0, 0.0, -1.0), 0.5))

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
