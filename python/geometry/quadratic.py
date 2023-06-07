from typing import Protocol


class Quadratic(Protocol):
    def get_side(self) -> int:
        raise NotImplementedError()
