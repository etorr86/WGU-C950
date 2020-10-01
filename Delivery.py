class Delivery:
    def __init__(self, distances, trucks):
        self._distancesList = distances
        self._trucksList = trucks
        self.status = 'In hub'

    def get_status(self):
        return self.status
