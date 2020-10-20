# imports --------------------------------------------------------------------------- #
import pygame

from ..functions import snap
from ..vector import Vector

# rect class ------------------------------------------------------------------------ #
class Rect:
    # initialisation ---------------------------------------------------------------- #
    def __init__(
        self,
        left: float,
        top: float,
        width: float,
        height: float,
        colour: tuple = (255, 255, 255),
        fill: bool = False,
    ):
        self.colour = colour
        self.height = height
        self.fill = fill
        self.left = left
        self.top = top
        self.width = width

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
    def bottom(self):
        return self.__top + self.__height

    @bottom.setter
    def bottom(self, bottom):
        if type(bottom) not in (float, int):
            raise TypeError

        if type(height) != float:
            height = float(height)

        snap(bottom, 1)

        self.__height = bottom - self.__top

    @property
    def bottom_left(self):
        return Vector(self.__left, self.bottom)

    @bottom_left.setter
    def bottom_left(self, bottom_left):
        if type(bottom_left) != type(Vector()):
            raise TypeError

        bottom_left.snap(1)

        self.__height = bottom_left.y - self.__top
        self.__left = bottom_left.x

    @property
    def bottom_right(self):
        return Vector(self.right, self.bottom)

    @bottom_right.setter
    def bottom_right(self, bottom_right):
        if type(bottom_right) != type(Vector()):
            raise TypeError

        bottom_right.snap(1)

        self.__height = bottom_right.y - self.__top
        self.__width = bottom_right.x - self.__left

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
    def fill(self):
        return self.__fill

    @fill.setter
    def fill(self, fill):
        if type(fill) != bool:
            raise TypeError

        self.__fill = fill

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) not in (float, int):
            raise TypeError

        if type(height) != float:
            height = float(height)

        snap(height, 1)

        self.__height = height

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        if type(left) not in (float, int):
            raise TypeError

        if type(left) != float:
            left = float(left)

        snap(left, 1)

        self.__left = left

    @property
    def right(self):
        return self.__left + self.__width

    @right.setter
    def right(self, right):
        if type(right) not in (float, int):
            raise TypeError

        if type(right) != float:
            right = float(right)

        snap(right, 1)

        self.__width = right - self.__left

    @property
    def size(self):
        return Vector(self.__width, self.__height)

    @size.setter
    def size(self, size):
        if type(size) != type(Vector()):
            raise TypeError

        size.snap(1)

        self.__height = size.y
        self.__width = size.x

    @property
    def top(self):
        return self.__top

    @top.setter
    def top(self, top):
        if type(top) not in (float, int):
            raise TypeError

        if type(top) != float:
            top = float(top)

        snap(top, 1)

        self.__top = top

    @property
    def top_left(self):
        return Vector(self.__left, self.__top)

    @top_left.setter
    def top_left(self, top_left):
        if type(top_left) != type(Vector()):
            raise TypeError

        top_left.snap(1)

        self.__left = top_left.x
        self.__top = top_left.y

    @property
    def top_right(self):
        return Vector(self.right, self.__top)

    @top_right.setter
    def top_right(self, top_right):
        if type(top_right) != type(Vector()):
            raise TypeError

        top_right.snap(1)

        self.__top = top_right.y
        self.__width = top_right.x - self.__left

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) not in (float, int):
            raise TypeError

        if type(width) != float:
            width = float(width)

        snap(width, 1)

        self.__width = width

    # methods ----------------------------------------------------------------------- #
    def copy(self):
        return Rect(self.left, self.top, self.width, self.height)

    def draw(self, surface):
        if not self.__fill:
            pygame.draw.lines(
                surface,
                self.__colour,
                True,
                [
                    [*self.top_left],
                    [*self.top_right - Vector(1, 0)],
                    [*self.bottom_right - Vector(1, 1)],
                    [*self.bottom_left - Vector(0, 1)],
                ],
            )
        else:
            pygame.draw.rect(
                surface, [*self.__colour, max(self.__alpha, 0)], self.pygame_rect()
            )

    def normalise(self):
        normalise = self.normalised()

        self.__height = normalise.height
        self.__left = normalise.left
        self.__top = normalise.top
        self.__width = normalise.width

    def normalised(self):
        normalised = self.copy()

        if normalised.right < normalised.left:
            normalised.left = normalised.right
            normalised.width = -normalised.width

        if normalised.bottom < normalised.top:
            normalised.top = normalised.bottom
            normalised.height = -normalised.height

        return normalised

    def pygame_rect(self):
        return pygame.Rect(self.left, self.top, self.width, self.height)

    def pygame_surface(self):
        return pygame.Surface([int(self.width), int(self.height)])
