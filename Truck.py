class Truck:
    def __init__(self, truck, package=None):
        self._truckId = truck
        if package is None:
            package = []
        self._truckPackage = package,

    def add_package(self, package):
        return self._truckPackage.__add__(package)

    def package(self):
        return self._truckPackage

    def truck(self):
        return self._truckId

