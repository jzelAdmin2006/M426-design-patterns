from threading import Lock


class ParkingLot:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.occupied = 0
        self.lock = Lock()

    def enter(self):
        with self.lock:
            if self.occupied < self.capacity:
                self.occupied += 1
            else:
                raise ValueError("parking lot is full")

    def exit(self):
        with self.lock:
            if self.occupied > 0:
                self.occupied -= 1
            else:
                raise ValueError("parking lot is empty")
