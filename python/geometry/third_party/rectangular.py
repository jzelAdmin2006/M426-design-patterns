from typing import Protocol


class Rectangular(Protocol):
    def get_width(self) -> int:
        raise NotImplementedError()

    def get_height(self) -> int:
        raise NotImplementedError()
