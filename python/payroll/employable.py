from typing import Protocol


class Employable(Protocol):
    def get_full_name(self):
        raise NotImplementedError()

    def get_salary(self):
        raise NotImplementedError()

    def add_note(self, kind: str, note: str):
        raise NotImplementedError()

    def get_note(self, kind: str) -> str:
        raise NotImplementedError()
