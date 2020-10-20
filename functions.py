# imports --------------------------------------------------------------------------- #
import math

from .vector import Vector


def bias(num, amount):
    if type(num) not in (float, int):
        raise TypeError

    if type(amount) not in (float, int):
        raise TypeError

    if num > amount:
        num -= amount
    elif num < -amount:
        num += amount
    else:
        num = 0

    return num


def rectangle_corners(points):
    if type(points) != tuple:
        raise TypeError

    if len(points) != 2:
        raise Exception

    for point in points:
        if type(point) != type(Vector()):
            raise TypeError

    point_1 = points[0]
    point_2 = points[1]
    top = Vector(min(point_1.x, point_2.x), min(point_1.y, point_2.y))
    bottom = Vector(max(point_1.x, point_2.x), max(point_1.y, point_2.y))

    return [top, bottom]


def sign(num):
    if type(num) not in (float, int):
        raise TypeError

    if num == 0:
        return 1

    return num // abs(num)

def snap(num, other):
    return math.floor(num / other + 0.5) * other
