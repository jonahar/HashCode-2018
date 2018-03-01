import sys
import Parser
import random


def get_best_car(k_cars, ride):
    # gets fastest reaching car to this ride:
    best_time = -100
    best_car = None
    for car in k_cars:
        cur_time = car.check_availability(ride)
        if (best_time == -100 or best_time > cur_time):
            best_time = cur_time
            best_car = car
    return best_car


def get_score(car, ride):
    """
    Calculate the score we would get if we were to assign the ride to the car
    Assuming it can be assigned
    """
    score = ride.total_length()
    if car.check_availability(ride) == ride.start_time():
        score += bonus
    return score


input_filename = sys.argv[1]
output_filename = sys.argv[2]
rides, cars, bonus, num_rides, num_cars = Parser.build_data(input_filename)
rides.sort(key=lambda r: r.start_time())

m = 2
k = 2

for i in range(0, num_rides - m):
    # randomly select k cars
    k_cars = random.sample(cars, k)
    best_assign = {'car': None, 'ride': None, 'score': -1}
    for j in range(min(i + m, num_rides)):
        if rides[j].is_assigned():
            continue
        best_car = get_best_car(k_cars, rides[j])
        score = get_score(best_car, rides[j])
        if score > best_assign['score']:
            # found a better ride to assign
            best_assign = {'car': best_car, 'ride': rides[j], 'score': score}
    if best_assign['score'] > 0:
        best_car.add_ride(best_assign['ride'])
        best_assign['ride'].assign()

# write results to output file
out_file = open(output_filename, 'w')
for car in cars:
    car.write_to_file(out_file)
out_file.close()
