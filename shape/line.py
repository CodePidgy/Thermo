# imports --------------------------------------------------------------------------- #
import math

import pygame

from .rect import Rect
from ..vector import Vector


# line class ------------------------------------------------------------------------ #
class Line:
    # initialisation ---------------------------------------------------------------- #
    def __init__(
        self,
        start: Vector,
        end: Vector,
        colour: tuple = (255, 255, 255),
        width: int = 1,
    ):
        self.colour = colour
        self.end = end
        self.start = start
        self.width = width

        self.__rect = None

    # properties -------------------------------------------------------------------- #
    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha):
        if type(alpha) not in (float, int):
            raise TypeError

        if type(alpha) != int:
            alpha = int(alpha)

        self.__alpha = alpha

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour):
        if type(colour) not in (list, tuple):
            raise TypeError

        if len(colour) > 4 or len(colour) < 3:
            raise Exception

        if type(colour) != tuple:
            colour = tuple(colour)

        self.__alpha = 255

        if len(colour) != 3:
            self.__alpha = colour[3]
            colour = colour[:3]

        self.__colour = colour

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        if type(end) != type(Vector()):
            raise TypeError

        self.__end = end

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        if type(start) != type(Vector()):
            raise TypeError

        self.__start = start

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) not in (float, int):
            raise TypeError

        if type(width) != int:
            width = int(width)

        self.__width = width

    # methods ----------------------------------------------------------------------- #
    def angle_to_normal(self, plane):
        if type(plane) != type(self):
            raise TypeError

        return math.radians(90) - (self.gradient() - plane.gradient())

    def draw(self, surface, offset=Vector(0, 0)):
        if type(surface) != type(pygame.Surface((0, 0))):
            raise TypeError

        if type(offset) != type(Vector()):
            raise TypeError

        pygame.draw.line(
            surface,
            [*self.__colour, max(self.__alpha, 0)],
            [*self.__start + offset],
            [*self.__end + offset],
            self.__width,
        )

    def gradient(self):
        return self.__end.angle_to(self.__start)

    def intersect(self, other):
        if type(other) != type(self):
            raise TypeError

        def orientation(a, b, c):
            val = (float(b.y - a.y) * (c.x - b.x)) - (float(b.x - a.x) * (c.y - b.y))

            if val > 0:
                return 1
            elif val < 0:
                return -1
            else:
                return 0

        def on_segment(a, b, c):
            if (
                (b.x <= max(a.x, c.x))
                and (b.x >= min(a.x, c.x))
                and (b.y <= max(a.y, c.y))
                and (b.y >= min(a.y, c.y))
            ):
                return True
            else:
                return False

        orientation_1 = orientation(self.__start, self.__end, other.start)
        orientation_2 = orientation(self.__start, self.__end, other.end)
        orientation_3 = orientation(other.start, other.end, self.__start)
        orientation_4 = orientation(other.start, other.end, self.__end)

        if orientation_1 != orientation_2 and orientation_3 != orientation_4:
            return True
        elif orientation_1 == 0 and on_segment(self.__start, other.start, self.__end):
            return True
        elif orientation_2 == 0 and on_segment(self.__start, other.end, self.__end):
            return True
        elif orientation_3 == 0 and on_segment(other.start, self.__start, other.end):
            return True
        elif orientation_4 == 0 and on_segment(other.start, self.__end, other.end):
            return True
        else:
            return False

    def intersect_point(self, other):
        if type(other) != type(self):
            raise TypeError

        if not self.intersect(other):
            return False

        value = (
            (self.__start.x - other.start.x) * (other.start.y - other.end.y)
            - (self.__start.y - other.start.y) * (other.start.x - other.end.x)
        ) / (
            (self.__start.x - self.__end.x) * (other.start.y - other.end.y)
            - (self.__start.y - self.__end.y) * (other.start.x - other.end.x)
        )

        return Vector(
            self.__start.x + value * (self.__end.x - self.__start.x),
            self.__start.y + value * (self.__end.y - self.__start.y),
        )

    def length(self):
        return math.sqrt(
            (self.__end.x - self.__start.x) ** 2 + (self.__end.y - self.__start.y) ** 2
        )

    def middle(self):
        return Vector(*(self.start + self.end) / 2)

    def normal(self, start):
        angle = self.gradient()

        if angle > math.radians(90):
            angle += math.radians(-180)
        elif angle < math.radians(-90):
            angle += math.radians(180)

        end = Vector(start.x - 1, start.y).rotate_around(
            angle + math.radians(90), start
        )

        return Line(start, end)

    def rect(self):
        sort = self.sorted_x()

        sort.start.snap(1)
        sort.end.snap(1)

        if sort.gradient() == 0:
            left = sort.start.x
            width = sort.end.x - sort.start.x + 1
            top = (sort.start.y - self.__width // 2) - (self.__width % 2 - 1)
            height = self.__width
        else:
            if not abs(sort.start.x - sort.end.x) <= abs(sort.start.y - sort.end.y):
                if sort.gradient() > 0:
                    left = sort.start.x
                    width = sort.end.x - left + 1
                    top = (sort.start.y - self.__width // 2) - (self.__width % 2 - 1)
                    height = sort.end.y - top + self.__width // 2 + 1
                else:
                    left = sort.start.x
                    width = sort.end.x - left + 1
                    top = (sort.end.y - self.__width // 2) - (self.__width % 2 - 1)
                    height = sort.start.y - top + self.__width // 2 + 1
            else:
                if sort.gradient() > 0:
                    left = (sort.start.x - self.__width // 2) - (self.__width % 2 - 1)
                    width = sort.end.x - left + self.__width // 2 + 1
                    top = sort.start.y
                    height = sort.end.y - top + 1
                else:
                    left = (sort.start.x - self.__width // 2) - (self.__width % 2 - 1)
                    width = sort.end.x - left + self.__width // 2 + 1
                    top = sort.end.y
                    height = sort.start.y - top + 1

        return Rect(left, top, width, height)

    def reflect(self, plane, magnitude=None):
        if not self.intersect(plane):
            return False

        if magnitude == None:
            magnitude = self.length

        start = self.intersect_point(plane)
        angle = plane.gradient() + math.radians(90) + self.angle_to_normal(plane)
        end = Vector(start.x - 1 * magnitude, start.y).rotate_around(angle, start)

        return Line(start, end)

    def reflect_vector(self, plane, magnitude=None):
        reflected = self.reflect(plane, magnitude)

        return reflected.end - reflected.start

    def side(self, point):
        sort = self.sorted_y()

        vec_1 = Vector(sort.end.x - sort.start.x, sort.end.y - sort.start.y)
        vec_2 = Vector(sort.end.x - point.x, sort.end.y - point.y)

        if sort.end.x > sort.start.x:
            if vec_1.x * vec_2.y - vec_1.y * vec_2.x > 0:
                return 1
            elif vec_1.x * vec_2.y - vec_1.y * vec_2.x < 0:
                return -1
            else:
                return 0
        elif sort.end.x < sort.start.x:
            if vec_1.x * vec_2.y - vec_1.y * vec_2.x < 0:
                return 1
            elif vec_1.x * vec_2.y - vec_1.y * vec_2.x > 0:
                return -1
            else:
                return 0
        else:
            return 0

    def snap(self, other):
        snap = self.snapped(other)

        self.__end = snap.end
        self.__start = snap.start

    def snapped(self, other):
        return Line(
            self.__start.snapped(other),
            self.__end.snapped(other),
            self.__colour,
            self.__width,
        )

    def sort_x(self):
        sort_x = self.sorted_x()

        self.__start = sort_x.start
        self.__end = sort_x.end

    def sorted_x(self):
        if self.__start.x > self.__end.x:
            return Line(self.__end, self.__start)

        return self

    def sort_y(self):
        sort_y = self.sorted_x()

        self.__start = sort_y.start
        self.__end = sort_y.end

    def sorted_y(self):
        if self.__start.y > self.__end.y:
            return Line(self.__end, self.__start)

        return self
