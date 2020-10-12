# imports --------------------------------------------------------------------------- #
import pygame

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
    ):
        self.colour = colour
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    # properties -------------------------------------------------------------------- #
    @property
    def alpha(self):
        # functionality ------------------------------------------------------------- #
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha):
        # sanity checks ------------------------------------------------------------- #
        if type(alpha) not in (float, int):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(alpha) != int:
            alpha = int(alpha)

        self.__alpha = alpha

    @property
    def bottom(self):
        # functionality ------------------------------------------------------------- #
        return self.top + self.height

    @property
    def bottom_left(self):
        # functionality ------------------------------------------------------------- #
        return Vector(self.left, self.bottom)

    @property
    def bottom_right(self):
        # functionality ------------------------------------------------------------- #
        return Vector(self.right, self.bottom)

    @property
    def centre(self):
        # functionality ------------------------------------------------------------- #
        return Vector(self.left + self.width / 2, self.top + self.height / 2)

    @property
    def colour(self):
        # functionality ------------------------------------------------------------- #
        return self.__colour

    @colour.setter
    def colour(self, colour):
        # sanity checks ------------------------------------------------------------- #
        if type(colour) not in (list, tuple):
            raise TypeError

        if len(colour) > 4 or len(colour) < 3:
            raise Exception

        # functionality ------------------------------------------------------------- #
        if type(colour) != tuple:
            colour = tuple(colour)

        self.__colour = colour

    @property
    def height(self):
        # functionality ------------------------------------------------------------- #
        return self.__height

    @height.setter
    def height(self, height):
        # sanity checks ------------------------------------------------------------- #
        if type(height) not in (float, int):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(height) != float:
            height = float(height)

        self.__height = height

    @property
    def left(self):
        # functionality ------------------------------------------------------------- #
        return self.__left

    @left.setter
    def left(self, left):
        # sanity checks ------------------------------------------------------------- #
        if type(left) not in (float, int):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(left) != float:
            left = float(left)

        self.__left = left

    @property
    def mid_bottom(self):
        # functionality ------------------------------------------------------------- #
        return Vector(self.left + self.width / 2, self.bottom)

    @property
    def mid_left(self):
        # functionality ------------------------------------------------------------- #
        return Vector(self.left, self.top + self.height / 2)

    @property
    def mid_right(self):
        # functionality ------------------------------------------------------------- #
        return Vector(self.right, self.top + self.height / 2)

    @property
    def mid_top(self):
        # functionality ------------------------------------------------------------- #
        return Vector(self.left + self.width / 2, self.top)

    @property
    def right(self):
        # functionality ------------------------------------------------------------- #
        return self.left + self.width

    @property
    def size(self):
        # functionality ------------------------------------------------------------- #
        return Vector(self.width, self.height)

    @property
    def top(self):
        # functionality ------------------------------------------------------------- #
        return self.__top

    @top.setter
    def top(self, top):
        # sanity checks ------------------------------------------------------------- #
        if type(top) not in (float, int):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(top) != float:
            top = float(top)

        self.__top = top

    @property
    def top_left(self):
        # functionality ------------------------------------------------------------- #
        return Vector(self.left, self.top)

    @property
    def top_right(self):
        # functionality ------------------------------------------------------------- #
        return Vector(self.right, self.top)

    @property
    def width(self):
        # functionality ------------------------------------------------------------- #
        return self.__width

    @width.setter
    def width(self, width):
        # sanity checks ------------------------------------------------------------- #
        if type(width) not in (float, int):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(width) != float:
            width = float(width)

        self.__width = width

    # methods ----------------------------------------------------------------------- #
    def copy(self):
        return Rect(self.left, self.top, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(
            surface, [*self.__colour, max(self.__alpha, 0)], self.pygame_rect()
        )

    def normalise(self):
        # functionality ------------------------------------------------------------- #
        normalise = self.normalised()

        self.__height = normalise.height
        self.__left = normalise.left
        self.__top = normalise.top
        self.__width = normalise.width

    def normalised(self):
        # functionality ------------------------------------------------------------- #
        normalised = self.copy()

        if normalised.right < normalised.left:
            normalised.left = normalised.right
            normalised.width = -normalised.width

        if normalised.bottom < normalised.top:
            normalised.top = normalised.bottom
            normalised.height = -normalised.height

        return normalised

    def pygame_rect(self):
        # functionality ------------------------------------------------------------- #
        return pygame.Rect(self.left, self.top, self.width, self.height)

    def pygame_surface(self):
        # functionality ------------------------------------------------------------- #
        return pygame.Surface([int(self.width), int(self.height)])
