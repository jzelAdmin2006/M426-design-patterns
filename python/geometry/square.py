from geometry.quadratic import Quadratic


class Square(Quadratic):
    def __init__(self, side: int):
        self.side = side

    def get_side(self) -> int:
        return self.side

    def __str__(self) -> str:
        return f"Square({self.side})"
