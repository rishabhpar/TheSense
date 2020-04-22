class SafeSpot:
    id = -1     # should hold values 1-100
    listOfSpotsOccupied = []
    covered = False

    def __init__(self, id, list, covered):
        self.id = id
        self.listOfSpotsOccupied = list
        self.covered = covered

    def get_id(self):
        return self.id

    def get_list(self):
        return self.listOfSpotsOccupied

    def is_covered(self):
        return self.covered
