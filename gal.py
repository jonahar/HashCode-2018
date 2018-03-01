

def get_score(car, ride):
    """
    Calculate the score we would get if we were to assign the ride to the car
    Assuming it can be assigned
    """
    score = ride.total_length()
    if car.check_availability(ride) == ride.start_time():
        score += B
    return score