class Car:
    def __init__(self):
        self.location = (0, 0)
        self.a_time = 0
        self.rides_history = []

    def check_availability(self, ride):
        """
        this function returns how soon the car can reach the given ride
        """
        dist = self.distance(ride.start_point())
        length = ride.total_length()
        if ((dist + length + self.a_time) <= ride.end_time()):
            return dist + self.a_time
        else:
            return -1

    def add_ride(self, ride):
        # checking car availability
        arrival = self.check_availability(ride)
        if (arrival < 0):
            return False
        else:
            self.a_time = arrival + ride.total_length()
            self.location = ride.end_point()
            self.rides_history.append(ride.get_index())
            return True

    def distance(self, location):
        """
        calculating location from the given point
        """
        x, y = location
        return abs(self.location[0] - x) + abs(self.location[1] - y)

    def write_to_file(self, file):
        file.write(str(len(self.rides_history)))
        for x in self.rides_history:
            file.write(' ')
            file.write(str(x))

        file.write("/n")


