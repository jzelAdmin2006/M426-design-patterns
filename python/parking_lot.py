from random import randint
from threading import Thread
from time import sleep

from parking_lot.parking_lot import ParkingLot

MAX_FILL_INTERVAL_MILLIS = 1000
MAX_EMPTY_INTERVAL_MILLIS = 2000
INITIAL_FILL_PHASE_MILLIS = 5000
REFRESH_DISPLAY_INTERVAL_MILLIS = 250


def main():
    lot = ParkingLot("Bahnhof Parking", 100)
    fill_thread = Thread(group=None, target=fill, args=(lot,))
    empty_thread = Thread(group=None, target=empty, args=(lot,))
    display_thread = Thread(group=None, target=display_state, args=(lot,))

    display_thread.start()
    fill_thread.start()
    sleep(INITIAL_FILL_PHASE_MILLIS)
    empty_thread.start()

    fill_thread.join()
    empty_thread.join()
    display_thread.join()


def fill(lot: ParkingLot):
    while lot.occupied < lot.capacity:
        lot.enter()
        sleep(randint(1, MAX_FILL_INTERVAL_MILLIS) / 1000.0)
        print(f"A car entered the lot '{lot.name}'.")


def empty(lot: ParkingLot):
    while lot.occupied > 0:
        lot.exit()
        sleep(randint(1, MAX_EMPTY_INTERVAL_MILLIS) / 1000.0)
        print(f"A car left the lot '{lot.name}'.")


def display_state(lot: ParkingLot):
    while True:
        print(f"{lot.name}: {lot.occupied}/{lot.capacity} occupied")
        sleep(randint(1, REFRESH_DISPLAY_INTERVAL_MILLIS) / 1000.0)


if __name__ == "__main__":
    main()
