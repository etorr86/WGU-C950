from Truck import Truck


class Delivery:
    def __init__(self, distances, trucks, packages):
        self._distancesList = distances
        self._trucksList = [Truck()] * trucks
        self._packageList = packages

    def get_status(self):
        return 'self.status'

    def start_delivery(self):
        return "Delivery"

    def arrange_trucks(self):
        self._trucksList[0].add_package(self._packageList.find('19'))
        self._trucksList[1].add_package(self._packageList.find('2'))
        self._trucksList[1].add_package(self._packageList.find('5'))
        self._trucksList[1].add_package(self._packageList.find('8'))
        self._trucksList[1].add_package(self._packageList.find('24'))

        for keyItem in self._packageList.keys():
            if '10:30:00 AM' or '9:00:00 AM' in self._packageList.find(keyItem).package_delivery_time():
                self._trucksList[0].add_package(self._packageList.find(keyItem))
            else:
                self._trucksList[0].add_package(self._packageList.find(keyItem))
        print(self._trucksList[0])
