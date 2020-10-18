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
        if type(other) not in (float, int, type(self)):
            raise TypeError

        if type(other) == type(self):
            added = tuple(a + b for a, b in zip(self, other))
        else:
            added = tuple(a + other for a in self)

        return Vector(*added)

    def __floordiv__(self, other):
        if type(other) not in (float, int, type(self)):
            raise TypeError

        if type(other) == type(self):
            divided = tuple(a // b for a, b in zip(self, other))
        else:
            divided = tuple(a // other for a in self)

        return Vector(*divided)

    def __mul__(self, other):
        if type(other) not in (float, int, type(self)):
            raise TypeError

        if type(other) == type(self):
            mulled = tuple(a * b for a, b in zip(self, other))
        else:
            mulled = tuple(a * other for a in self)

        return Vector(*mulled)

    def __radd__(self, other):
        if type(other) not in (float, int, type(self)):
            raise TypeError

        if type(other) == type(self):
            added = tuple(b + a for a, b in zip(self, other))
        else:
            added = tuple(other + a for a in self)

        return Vector(*added)

    def __rfloordiv__(self, other):
        if type(other) not in (float, int, type(self)):
            raise TypeError

        if type(other) == type(self):
            divided = tuple(b // a for a, b in zip(self, other))
        else:
            divided = tuple(other // a for a in self)

        return Vector(*divided)

    def __rmul__(self, other):
        if type(other) not in (float, int, type(self)):
            raise TypeError

        if type(other) == type(self):
            mulled = tuple(b * a for a, b in zip(self, other))
        else:
            mulled = tuple(other * a for a in self)

        return Vector(*mulled)

    def __rsub__(self, other):
        if type(other) not in (float, int, type(self)):
            raise TypeError

        if type(other) == type(self):
            subbed = tuple(b - a for a, b in zip(self, other))
        else:
            subbed = tuple(other - a for a in self)

        return Vector(*subbed)

    def __rtruediv__(self, other):
        if type(other) not in (float, int, type(self)):
            raise TypeError

        if type(other) == type(self):
            divided = tuple(b / a for a, b in zip(self, other))
        else:
            divided = tuple(other / a for a in self)

        return Vector(*divided)

    def __sub__(self, other):
        if type(other) not in (float, int, type(self)):
            raise TypeError

        if type(other) == type(self):
            subbed = tuple(a - b for a, b in zip(self, other))
        else:
            subbed = tuple(a - other for a in self)

        return Vector(*subbed)

    def __truediv__(self, other):
        if type(other) not in (float, int, type(self)):
            raise TypeError

        if type(other) == type(self):
            divided = tuple(a / b for a, b in zip(self, other))
        else:
            divided = tuple(a / other for a in self)

        return Vector(*divided)

    # comparison operations --------------------------------------------------------- #
    def __eq__(self, other):
        if type(other) != type(self):
            if other == None:
                return False
            raise TypeError

        if self.__x == other.x and self.__y == other.y:
            return True

        return False

    def __ge__(self, other):
        if type(other) != type(self):
            raise TypeError

        if self.__x > other.x:
            return True
        elif self.__x == other.x:
            if self.__y > other.y:
                return True
            elif self.__y == other.y:
                return True

        return False

    def __gt__(self, other):
        if type(other) != type(self):
            raise TypeError

        if self.__x > other.x:
            return True
        elif self.__x == other.x:
            if self.__y > other.y:
                return True

        return False

    def __le__(self, other):
        if type(other) != type(self):
            raise TypeError

        if self.__x < other.x:
            return True
        elif self.__x == other.x:
            if self.__y < other.y:
                return True
            elif self.__y == other.y:
                return True

        return False

    def __lt__(self, other):
        if type(other) != type(self):
            raise TypeError

        if self.__x < other.x:
            return True
        elif self.__x == other.x:
            if self.__y < other.y:
                return True

        return False

    # conversion operations --------------------------------------------------------- #
    def __abs__(self):
        return Vector(abs(self.__x), abs(self.__y))

    def __round__(self):
        return Vector(round(self.__x), round(self.__y))

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    # other operations -------------------------------------------------------------- #
    def __iter__(self):
        return (self.__x, self.__y).__iter__()

    # properties -------------------------------------------------------------------- #
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) not in (float, int):
            raise TypeError

        if type(x) != float:
            x = float(x)

        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) not in (float, int):
            raise TypeError

        if type(y) != float:
            y = float(y)

        self.__y = y

    # methods ----------------------------------------------------------------------- #
    def angle(self):
        return math.atan2(self.__y, self.__x)

    def angle_to(self, other):
        if type(other) != type(self):
            raise TypeError

        return (self - other).angle()

    def ceil(self):
        ceil = self.ceiled()

        self.__x = ceil.x
        self.__y = ceil.y

    def ceiled(self):
        return Vector(math.ceil(self.__x), math.ceil(self.__y))

    def clamp(self, value):
        if type(value) not in (float, int):
            raise TypeError

        clamp = self.clamped(value)

        self.__x = clamp.x
        self.__y = clamp.y

    def clamped(self, value):
        if type(value) not in (float, int):
            raise TypeError

        clamp = self
        magnitude = self.magnitude()

        if magnitude > 0 and value < magnitude:
            clamp /= magnitude
            clamp *= value

        return Vector(*clamp)

    def copy(self):
        return Vector(self.__x, self.__y)

    def cross(self, other):
        if type(other) != type(self):
            raise TypeError

        cross = self.crossed(other)

        self.__x = cross.x
        self.__y = cross.y

    def crossed(self, other):
        if type(other) != type(self):
            raise TypeError

        return self.__x * other.y - self.__y * other.x

    def direction_to(self, other):
        if type(other) != type(self):
            raise TypeError

        return Vector(other.x - self.__x, other.y - self.__y).normalised()

    def distance_to(self, other):
        if type(other) != type(self):
            raise TypeError

        return math.sqrt((self.__x - other.x) ** 2 + (self.__y - other.y) ** 2)

    def distance_squared_to(self, other):
        if type(other) != type(self):
            raise TypeError

        return (self.__x - other.x) ** 2 + (self.__y - other.y) ** 2

    def dot(self, other):
        if type(other) != type(self):
            raise TypeError

        return self.__x * other.x + self.__y * other.y

    def floor(self):
        floor = self.floored()

        self.__x = floor.x
        self.__y = floor.y

    def floored(self):
        return Vector(math.floor(self.__x), math.floor(self.__y))

    def is_equal_approx(self, other):
        if type(other) != type(self):
            raise TypeError

        return math.isclose(self.__x, other.x, 0.00001) and math.isclose(
            self.__y, other.y, 0.00001
        )

    def is_normalised(self):
        return math.isclose(self.magnitude_squared, 1, abs_tol=0.00001)

    def magnitude(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    def magnitude_squared(self):
        return self.__x ** 2 + self.__y ** 2

    def normalise(self):
        normalise = self.normalised()

        self.__x = normalise.x
        self.__y = normalise.y

    def normalised(self):
        return self / self.magnitude()

    def rotate(self, angle):
        if type(angle) not in (float, int):
            raise TypeError

        cos = math.cos(angle)
        sin = math.sin(angle)

        return Vector(self.__x * cos - self.__y * sin, self.__x * sin + self.__y * cos)

    def rotate_around(self, angle, point):
        if type(angle) not in (float, int):
            raise TypeError

        if type(point) != type(self):
            raise TypeError

        cos = math.cos(angle)
        sin = math.sin(angle)

        x = self.x - point.x
        y = self.y - point.y

        return Vector((x * cos - y * sin) + point.x, (x * sin + y * cos) + point.y)

    def sign(self):
        sign = lambda a: a and (1, -1)[a < 0]

        return Vector(sign(self.__x), sign(self.__y))

    def snap(self, other):
        if type(other) not in (int, type(self)):
            raise TypeError

        snap = self.snapped(other)

        self.__x = snap.x
        self.__y = snap.y

    def snapped(self, other):
        if type(other) not in (int, type(self)):
            raise TypeError

        if type(other) != type(self):
            other = Vector(other, other)

        step = lambda value, other: math.floor(value / other + 0.5) * other

        return Vector(step(self.__x, other.x), step(self.__y, other.y))
