from geometry.quadratic import Quadratic
from geometry.third_party.rectangular import Rectangular


class RectangleAdapter(Rectangular):
    def __init__(self, square: Quadratic):
        self.square = square

    def get_width(self) -> int:
        return self.square.get_side()

    def get_height(self) -> int:
        return self.square.get_side()
