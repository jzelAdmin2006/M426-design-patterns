from geometry.square import Square
from geometry.rectangle_adapter import RectangleAdapter
from geometry.third_party.calculator import get_area
from geometry.third_party.calculator import get_diagonal
from geometry.third_party.calculator import get_perimeter
from geometry.third_party.rectangle import Rectangle

if __name__ == "__main__":
    rectangle = Rectangle(3, 4)
    print(rectangle)
    print(f"Area:\t\t{get_area(rectangle)}")
    print(f"Perimeter:\t{get_perimeter(rectangle)}")
    print(f"Diagonal:\t{get_diagonal(rectangle)}")

    square = Square(3)
    rect_square = RectangleAdapter(square)
    print(f"Area:\t\t{get_area(rect_square)}")
    print(f"Perimeter:\t{get_perimeter(rect_square)}")
    print(f"Diagonal:\t{get_diagonal(rect_square)}")
