import itertools


class Truck:
    id_generator = itertools.count(1)

    def __init__(self, package=None):
        self._truckId = next(self.id_generator)
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

    # Return the Truck Id
    def truck(self):
        return self._truckId
