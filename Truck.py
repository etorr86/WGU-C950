import itertools


class Truck:
    id_generator = itertools.count(1)

    def __init__(self, package=None, startTime=None):
        self._truckId = next(self.id_generator)
        self._truckStartTime = startTime
        self._totalDistance = 0
        if package is None:
            package = []
        self._truckPackage = package

    # Return the list of packages
    def package_list(self):
        return self._truckPackage

    # Return a package based on ID
    # Time-Complexity is O(n) because there is a loop present
    def package(self, packageId):
        for package in self._truckPackage:
            if package.package_key() != packageId:
                continue
            else:
                return package
        return None

    # Add package to the list of packages
    def add_package(self, package):
        self._truckPackage.append(package)

    def remove_package(self, package):
        removed_package = self._truckPackage.index(package)
        self._truckPackage.pop(removed_package)

    # Return the Truck Id
    def truck(self):
        return self._truckId

    def total_distance(self):
        return self._totalDistance

    def add_distance(self, distance):
        self._totalDistance += distance
        return self._totalDistance

    # Return the truck start time
    def truck_start_time(self):
        return self._truckStartTime

    def add_start_time(self, startTime):
        self._truckStartTime = startTime
