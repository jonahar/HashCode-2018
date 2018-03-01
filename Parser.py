from Tokenizer import Tokenizer
from Ride import Ride
import Car


def build_data(input_file):
    tokenizer = Tokenizer(input_file)
    rows = tokenizer.next_int()
    cols = tokenizer.next_int()
    num_cars = tokenizer.next_int()
    num_rides = tokenizer.next_int()
    bonus = tokenizer.next_int()
    total_steps = tokenizer.next_int()
    tokenizer.next_line()
    # building all rides
    rides = []
    for i in range(num_rides):
        a = tokenizer.next_int()
        b = tokenizer.next_int()
        x = tokenizer.next_int()
        y = tokenizer.next_int()
        s = tokenizer.next_int()
        f = tokenizer.next_int()
        rides.append(Ride(a, b, x, y, s, f))
    Car.T = total_steps
    cars = []
    for i in range(num_cars):
        cars.append(Car.Car())
    return rides, cars, bonus

