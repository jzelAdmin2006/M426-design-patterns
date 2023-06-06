from math import pow
from math import sqrt

from .rectangular import Rectangular


def get_area(rectangle: Rectangular) -> int:
    return rectangle.get_width() * rectangle.get_height()


def get_perimeter(rectangle: Rectangular) -> int:
    return 2 * rectangle.get_width() + 2 * rectangle.get_height()


def get_diagonal(rectangle: Rectangular) -> float:
    return sqrt(pow(rectangle.get_height(), 2.0) + pow(rectangle.get_width(), 2.0))
