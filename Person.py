class Person:
    x = -1
    y = -1
    safe = True  # use 0 - 359 where 0 is exactly east and then go CCW

    def __init__(self, x, y, safe):
        self.x = x
        self.y = y
        self.safe = safe

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def is_safe(self):
        return self.safe