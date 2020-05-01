class SafeSpot:
    id = -1     # should hold values 1-100
    listOfSpotsOccupied = []
    completelyUnsafe = False
    completelySafe = False
    locationCenter = []
    count = 0
    isCrossWind = False

    def __init__(self, id, list, number):
        self.id = id
        self.listOfSpotsOccupied = list
        self.count = number

    def get_id(self):
        return self.id

    def get_list(self):
        return self.listOfSpotsOccupied

