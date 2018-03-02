import sys
import Parser
import random


def get_best_car(k_cars, ride):
    # gets fastest reaching car to this ride:
    best_time = -100
    best_car = None
    for car in k_cars:
        cur_time = car.check_availability(ride)
        if (best_time == -100 or best_time > cur_time) and cur_time != -1:
            best_time = cur_time
            best_car = car
    return best_car


def get_score(car, ride):
    """
    Calculate the score we would get if we were to assign the ride to the car
    Assuming it can be assigned
    """
    score = ride.total_length()
    starting_ride_at = car.check_availability(ride)
    score = score - (starting_ride_at - car.a_time)
    if starting_ride_at == ride.start_time():
        score += bonus
    return score


input_file = sys.argv[1]
output_filename = sys.argv[2]
rides, cars, bonus, num_rides, num_cars = Parser.build_data(input_file)
rides.sort(key=lambda r: r.start_time())

m = 5  # window size of rides: number of rides from which we choose the next ride to assign
k = 20  # number of cars to check for each ride

for i in range(0, num_rides):
    # randomly select k cars
    k_cars = random.sample(cars, k)
    best_assign = {'car': None, 'ride': None, 'score': -1}
    for j in range(min(i + m, num_rides)):
        if rides[j].is_assigned():
            continue
        best_car = get_best_car(k_cars, rides[j])
        if best_car is None:
            continue
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
