from .rectangular import Rectangular


class Rectangle(Rectangular):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def __str__(self):
        return f"Rectangle({self.height}, {self.width})"
