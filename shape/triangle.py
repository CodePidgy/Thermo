# imports --------------------------------------------------------------------------- #
import math

from .line import Line
from ..vector import Vector

# triangle class -------------------------------------------------------------------- #
class Triangle:
    # initialisation ---------------------------------------------------------------- #
    def __init__(self, top: Vector, left: Vector, right: Vector):
        self.bottom_line = Line(left, right)
        self.left_line = Line(top, left)
        self.right_line = Line(top, right)

    # properties -------------------------------------------------------------------- #
    @property
    def bottom_line(self):
        return self.__bottom_line

    @bottom_line.setter
    def bottom_line(self, bottom_line):
        self.__bottom_line = bottom_line

    @property
    def left(self):
        return self.__bottom_line.start

    @left.setter
    def left(self, left):
        if type(left) != type(Vector()):
            raise TypeError

        self.__bottom_line.start = left.snapped(1)
        self.__left_line.end = left.snapped(1)

    @property
    def left_line(self):
        return self.__left_line

    @left_line.setter
    def left_line(self, left_line):
        self.__left_line = left_line

    @property
    def right(self):
        return self.__bottom_line.end

    @right.setter
    def right(self, right):
        if type(right) != type(Vector()):
            raise TypeError

        self.__bottom_line.start = right.snapped(1)
        self.__right_line.end = right.snapped(1)

    @property
    def right_line(self):
        return self.__right_line

    @right_line.setter
    def right_line(self, right_line):
        self.__right_line = right_line

    @property
    def top(self):
        return self.__left_line.start

    @top.setter
    def top(self, top):
        if type(top) != type(Vector()):
            raise TypeError

        self.__left_line.start = top.snapped(1)
        self.__right_line.start = top.snapped(1)

    # methods ----------------------------------------------------------------------- #
    # def bottom_line(self):
    #     return Line(self.__left, self.__right)

    def draw(self, surface):
        self.bottom_line.draw(surface)
        self.left_line.draw(surface)
        self.right_line.draw(surface)

    # def left_line(self):
    #     return Line(self.__top, self.__left)

    def normalise(self):
        normalise = self.normalised()

        self.__bottom_line = normalise.bottom_line
        self.__left_line = normalise.left_line
        self.__right_line = normalise.right_line

    def normalised(self):
        if self.top.y > self.left.y or self.top.y > self.right.y:
            if self.left.y > self.right.y:
                if self.__right_line.gradient() < self.__bottom_line.gradient():
                    left = self.left
                    right = self.top
                    top = self.right
                else:
                    left = self.top
                    right = self.left
                    top = self.right
            else:
                if self.__right_line.gradient() < self.__bottom_line.gradient():
                    left = self.top
                    right = self.right
                    top = self.left
                else:
                    left = self.right
                    right = self.top
                    top = self.left
        else:
            if self.left.y > self.right.y:
                if (
                    self.__left_line.gradient() - math.pi
                    > self.__bottom_line.gradient()
                ):
                    left = self.right
                    right = self.left
                    top = self.top
                else:
                    left = self.left
                    right = self.right
                    top = self.top
            else:
                if self.__right_line.gradient() < self.__bottom_line.gradient():
                    left = self.right
                    right = self.left
                    top = self.top
                else:
                    left = self.left
                    right = self.right
                    top = self.top

        return Triangle(top, left, right)

    # def right_line(self):
    #     return Line(self.__top, self.__right)
