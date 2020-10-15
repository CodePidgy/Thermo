# imports --------------------------------------------------------------------------- #
import math

# vector class ---------------------------------------------------------------------- #
class Vector:
    # initialisation ---------------------------------------------------------------- #
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    # mathematical operations ------------------------------------------------------- #
    def __add__(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) not in (float, int, type(self)):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(other) == type(self):
            added = tuple(a + b for a, b in zip(self, other))
        else:
            added = tuple(a + other for a in self)

        return Vector(*added)

    def __floordiv__(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) not in (float, int, type(self)):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(other) == type(self):
            divided = tuple(a // b for a, b in zip(self, other))
        else:
            divided = tuple(a // other for a in self)

        return Vector(*divided)

    def __mul__(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) not in (float, int, type(self)):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(other) == type(self):
            mulled = tuple(a * b for a, b in zip(self, other))
        else:
            mulled = tuple(a * other for a in self)

        return Vector(*mulled)

    def __radd__(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) not in (float, int, type(self)):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(other) == type(self):
            added = tuple(b + a for a, b in zip(self, other))
        else:
            added = tuple(other + a for a in self)

        return Vector(*added)

    def __rfloordiv__(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) not in (float, int, type(self)):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(other) == type(self):
            divided = tuple(b // a for a, b in zip(self, other))
        else:
            divided = tuple(other // a for a in self)

        return Vector(*divided)

    def __rmul__(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) not in (float, int, type(self)):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(other) == type(self):
            mulled = tuple(b * a for a, b in zip(self, other))
        else:
            mulled = tuple(other * a for a in self)

        return Vector(*mulled)

    def __rsub__(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) not in (float, int, type(self)):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(other) == type(self):
            subbed = tuple(b - a for a, b in zip(self, other))
        else:
            subbed = tuple(other - a for a in self)

        return Vector(*subbed)

    def __rtruediv__(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) not in (float, int, type(self)):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(other) == type(self):
            divided = tuple(b / a for a, b in zip(self, other))
        else:
            divided = tuple(other / a for a in self)

        return Vector(*divided)

    def __sub__(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) not in (float, int, type(self)):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(other) == type(self):
            subbed = tuple(a - b for a, b in zip(self, other))
        else:
            subbed = tuple(a - other for a in self)

        return Vector(*subbed)

    def __truediv__(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) not in (float, int, type(self)):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(other) == type(self):
            divided = tuple(a / b for a, b in zip(self, other))
        else:
            divided = tuple(a / other for a in self)

        return Vector(*divided)

    # comparison operations --------------------------------------------------------- #
    def __eq__(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) != type(self):
            if other == None:
                return False
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if self.__x == other.x and self.__y == other.y:
            return True

        return False

    def __ge__(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) != type(self):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if self.__x > other.x:
            return True
        elif self.__x == other.x:
            if self.__y > other.y:
                return True
            elif self.__y == other.y:
                return True

        return False

    def __gt__(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) != type(self):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if self.__x > other.x:
            return True
        elif self.__x == other.x:
            if self.__y > other.y:
                return True

        return False

    def __le__(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) != type(self):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if self.__x < other.x:
            return True
        elif self.__x == other.x:
            if self.__y < other.y:
                return True
            elif self.__y == other.y:
                return True

        return False

    def __lt__(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) != type(self):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if self.__x < other.x:
            return True
        elif self.__x == other.x:
            if self.__y < other.y:
                return True

        return False

    # conversion operations --------------------------------------------------------- #
    def __abs__(self):
        # functionality ------------------------------------------------------------- #
        return Vector(abs(self.__x), abs(self.__y))

    def __round__(self):
        # functionality ------------------------------------------------------------- #
        return Vector(round(self.__x), round(self.__y))

    def __str__(self):
        # functionality ------------------------------------------------------------- #
        return f"({self.__x}, {self.__y})"

    # other operations -------------------------------------------------------------- #
    def __iter__(self):
        # functionality ------------------------------------------------------------- #
        return (self.__x, self.__y).__iter__()

    # properties -------------------------------------------------------------------- #
    @property
    def angle(self):
        # functionality ------------------------------------------------------------- #
        return math.atan2(self.__y, self.__x)

    @property
    def angle_to(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) != type(self):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        return (self - other).angle

    @property
    def aspect(self):
        # functionality ------------------------------------------------------------- #
        return self.__x / self.__y

    @property
    def length(self):
        # functionality ------------------------------------------------------------- #
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    @property
    def length_squared(self):
        # functionality ------------------------------------------------------------- #
        return self.__x ** 2 + self.__y ** 2

    @property
    def sign(self):
        # functionality ------------------------------------------------------------- #
        sign = lambda a: a and (1, -1)[a < 0]

        return Vector(sign(self.__x), sign(self.__y))

    @property
    def tangent(self):
        # functionality ------------------------------------------------------------- #
        return Vector(self.__y, -self.__x)

    @property
    def x(self):
        # functionality ------------------------------------------------------------- #
        return self.__x

    @x.setter
    def x(self, x):
        # sanity checks ------------------------------------------------------------- #
        if type(x) not in (float, int):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(x) != float:
            x = float(x)

        self.__x = x

    @property
    def y(self):
        # functionality ------------------------------------------------------------- #
        return self.__y

    @y.setter
    def y(self, y):
        # sanity checks ------------------------------------------------------------- #
        if type(y) not in (float, int):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(y) != float:
            y = float(y)

        self.__y = y

    # methods ----------------------------------------------------------------------- #
    def ceil(self):
        # functionality ------------------------------------------------------------- #
        ceil = self.ceiled()

        self.__x = ceil.x
        self.__y = ceil.y

    def ceiled(self):
        # functionality ------------------------------------------------------------- #
        return Vector(math.ceil(self.__x), math.ceil(self.__y))

    def clamp(self, value):
        # sanity checks ------------------------------------------------------------- #
        if type(value) not in (float, int):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        clamp = self.clamped(value)

        self.__x = clamp.x
        self.__y = clamp.y

    def clamped(self, value):
        # sanity checks ------------------------------------------------------------- #
        if type(value) not in (float, int):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        clamp = self
        length = self.length()

        if length > 0 and value < length:
            clamp /= length
            clamp *= value

        return Vector(*clamp)

    def copy(self):
        # functionality ------------------------------------------------------------- #
        return Vector(self.__x, self.__y)

    def cross(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) != type(self):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        cross = self.crossed(other)

        self.__x = cross.x
        self.__y = cross.y

    def crossed(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) != type(self):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        return self.__x * other.y - self.__y * other.x

    def direction_to(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) != type(self):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        return Vector(other.x - self.__x, other.y - self.__y).normalised()

    def distance_to(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) != type(self):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        return math.sqrt((self.__x - other.x) ** 2 + (self.__y - other.y) ** 2)

    def distance_squared_to(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) != type(self):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        return (self.__x - other.x) ** 2 + (self.__y - other.y) ** 2

    def dot(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) != type(self):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        dot = self.dotted(other)

        self.__x = dot.x
        self.__y = dot.y

    def dotted(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) != type(self):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        return self.__x * other.x + self.__y * other.y

    def floor(self):
        # functionality ------------------------------------------------------------- #
        floor = self.floored()

        self.__x = floor.x
        self.__y = floor.y

    def floored(self):
        # functionality ------------------------------------------------------------- #
        return Vector(math.floor(self.__x), math.floor(self.__y))

    def is_equal_approx(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) != type(self):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        epsilon = 0.00001

        return math.isclose(self.__x, other.x, epsilon) and math.isclose(
            self.__y, other.y, epsilon
        )

    def is_normalised(self):
        # functionality ------------------------------------------------------------- #
        epsilon = 0.00001

        return math.isclose(self.length_squared, 1, abs_tol=epsilon)

    def normalise(self):
        # functionality ------------------------------------------------------------- #
        normalise = self.normalised()

        self.__x = normalise.x
        self.__y = normalise.y

    def normalised(self):
        # functionality ------------------------------------------------------------- #
        return self / self.length

    def rotate(self, angle):
        # sanity checks ------------------------------------------------------------- #
        if type(angle) not in (float, int):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        cos = math.cos(angle)
        sin = math.sin(angle)

        return Vector(self.__x * cos - self.__y * sin, self.__x * sin + self.__y * cos)

    def rotate_around(self, angle, point):
        # sanity checks ------------------------------------------------------------- #
        if type(angle) not in (float, int):
            raise TypeError

        if type(point) != type(self):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        cos = math.cos(angle)
        sin = math.sin(angle)

        x = self.x - point.x
        y = self.y - point.y

        return Vector((x * cos - y * sin) + point.x, (x * sin + y * cos) + point.y)

    def slide(self, normal):
        # sanity checks ------------------------------------------------------------- #
        if type(normal) != type(self):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        return self - normal * self.dot(normal)

    def snap(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) not in (int, type(self)):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        snap = self.snapped(other)

        self.__x = snap.x
        self.__y = snap.y

    def snapped(self, other):
        # sanity checks ------------------------------------------------------------- #
        if type(other) not in (int, type(self)):
            raise TypeError

        # functionality ------------------------------------------------------------- #
        if type(other) != type(self):
            other = Vector(other, other)

        step = lambda value, other: math.floor(value / other + 0.5) * other

        return Vector(step(self.__x, other.x), step(self.__y, other.y))
