from math import pow
from math import sqrt

from .rectangular import Rectangular


def get_area(rect: Rectangular) -> int:
    return rect.get_width() * rect.get_height()


def get_perimeter(rect: Rectangular) -> int:
    return 2 * rect.get_width() + 2 * rect.get_height()


def get_diagonal(rect: Rectangular) -> float:
    return sqrt(pow(rect.get_height(), 2.0) + pow(rect.get_width(), 2.0))
