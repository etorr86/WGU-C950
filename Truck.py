class Truck:
    def __init__(self, truck, package=None):
        self._truckId = truck
        if package is None:
            package = []
        self._truckPackage = package

    def package(self):
        return self._truckPackage

    def add_package(self, package):
        self._truckPackage.append(package)

    def truck(self):
        return self._truckId

