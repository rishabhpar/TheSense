class GasLeak:
    row = -1
    col = -1
    windDirection = 0       # use 0 - 359 where 0 is exactly north and then go CW

    def __init__(self, r, c, wd):
        self.row = r
        self.col = c
        self.windDirection = wd

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_direction(self):
        return self.windDirection
