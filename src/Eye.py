from Ray import *

class Eye:
    def __init__(self, origin, to, top, fov, aspect):
        halfHeight = math.tan(fov / 2)
        halfWidth = aspect * halfHeight
        self.origin = origin
        w = (origin - to).unit()
        u = top.cross(w).unit()
        v = w.cross(u)
        self.bottomLeft = Vector3(-halfWidth, -halfHeight, -1.0)
        self.horizontal = u * 2 * halfWidth
        self.vertical = v * 2 * halfHeight

    def getRay(self, u, v):
        return Ray(self.origin, self.bottomLeft + self.horizontal * u + self.vertical * v - self.origin)
