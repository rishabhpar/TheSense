class GasLeak:
    x = -1
    y = -1
    windDirection = 0       # use 0 - 359 where 0 is exactly east and then go CCW

    def __init__(self, x, y, wd):
        self.x = x
        self.y = y
        self.windDirection = wd

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_direction(self):
        return self.windDirection
