from Truck import Truck


class Delivery:
    def __init__(self, distances, trucks, packages):
        self._distancesList = distances
        self._trucksList = [Truck() for truck in range(trucks)]
        self._packageList = packages

    def get_status(self):
        return 'self.status'

    def start_delivery(self):
        return "Delivery"

    # Algorithm to arrange trucks
    # Time-Complexity is O(n) because a loop is present.
    def arrange_trucks(self):
        self._trucksList[0].add_package(self._packageList.find('19'))
        self._trucksList[1].add_package(self._packageList.find('2'))
        self._trucksList[1].add_package(self._packageList.find('5'))
        self._trucksList[1].add_package(self._packageList.find('8'))
        self._trucksList[1].add_package(self._packageList.find('24'))

        for keyItem in self._packageList.keys():
            if '10' in self._packageList.find(keyItem).package_delivery_time():
                self._trucksList[0].add_package(self._packageList.find(keyItem))
            elif '9' in self._packageList.find(keyItem).package_delivery_time():
                self._trucksList[0].add_package(self._packageList.find(keyItem))
            elif 'Wrong' in self._packageList.find(keyItem).package_notes():
                self._trucksList[0].add_package(self._packageList.find(keyItem))
            elif 'Can' in self._packageList.find(keyItem).package_notes():
                self._trucksList[1].add_package(self._packageList.find(keyItem))
            elif len(self._trucksList[2].package_list()) < 16:
                if (self._trucksList[0].package(keyItem) is None) and (self._trucksList[1].package(keyItem) is None):
                    self._trucksList[2].add_package(self._packageList.find(keyItem))
