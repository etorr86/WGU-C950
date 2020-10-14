# distance class, it acts as a model to use for the distance between packages.
class Distance:
    def __init__(self, address_from, address_to, distance):
        self._addressFrom = address_from,
        self._addressTo = address_to,
        self._totalDistance = distance

    def distance(self):
        return self._totalDistance

    def address_to(self):
        return "".join(self._addressTo[0].split("\n")[1:])

    def address_from(self):
        return "".join(self._addressFrom[0].split("\n")[1:])

    def place_name_to(self):
        return self._addressTo[0].split("\n")[0]

    def place_name_from(self):
        return self._addressFrom[0].split("\n")[0]
