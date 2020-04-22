class Person:
    row = -1
    col = -1
    id = 100 # should hold values starting at 101 increasing
    safe = True  # use 0 - 359 where 0 is exactly east and then go CCW

    def __init__(self, r, c, id, safe):
        self.row = r
        self.col = c
        self.id = id
        self.safe = safe

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def is_safe(self):
        return self.safe

    def get_id(self):
        return self.id
