from typing import Dict

from payroll.employable import Employable


class Employee(Employable):
    def __init__(self, first_name: str, last_name: str, salary: float):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.notes: Dict[str, str] = {}

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def add_note(self, kind: str, note: str):
        self.notes[kind] = note

    def get_note(self, kind: str) -> str:
        if kind not in self.notes:
            raise ValueError(f"no note of kind {kind} available")
        return self.notes[kind]

    def __str__(self) -> str:
        return self.get_full_name()
