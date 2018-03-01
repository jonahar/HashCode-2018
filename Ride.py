class Ride:
    def __init__(self, a, b, x, y, s, f):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f

    def start_point(self):
        return (self.a, self.b)

    def end_point(self):
        return (self.x, self.y)

    def start_time(self):
        return self.s

    def end_time(self):
        return self.f

    def total_length(self):
        return abs(self.y-self.b)+abs(self.x-self.a)
    # done?