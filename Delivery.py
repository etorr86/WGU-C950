class Delivery:
    def __init__(self, distances, trucks):
        self._distancesList = distances
        self._trucksList = trucks

    def get_status(self):
        return 'In Hub'
