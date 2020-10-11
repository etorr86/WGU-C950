from Truck import Truck
import datetime

HUB = "4001 South 700 East"
SPEED = 18


class Delivery:

    def __init__(self, distances, trucks, packages):
        self._distancesList = distances
        self._trucksList = [Truck() for truck in range(trucks)]
        self._optimizedTruckList = []
        self._packageList = packages

    def get_status_by_time(self, time):
        return 'self.status'

    def get_status_by_package(self, package, time):
        return 'self.status'

    # Loop over the optimized truck list then add and return their total distance
    # Time-Complexity is O(n) because a loop is present.
    def get_total_distance(self):
        total_distance = 0
        for truck in self._optimizedTruckList:
            total_distance += truck.total_distance()
        return "{0:.2f}".format(total_distance, 2)

    # main delivery function
    # Time-Complexity is O(n) because a loop is present.
    def start_delivery(self):
        self.arrange_trucks()
        # Call a function to optimized each truck
        for truck in self._trucksList:
            optimized_truck = Truck()
            optimized_truck.add_start_time(truck.truck_start_time())
            optimized_truck.add_time_to_delivery_map(truck.truck_start_time())
            ready_truck = self.optimize_delivery(HUB, truck, optimized_truck)
            self._optimizedTruckList.append(ready_truck)

        # call function to put times for each package delivered
        for truck in self._optimizedTruckList:
            self.set_delivery_time(truck)
        return "Delivery"

    # Algorithm to arrange trucks
    # Time-Complexity is O(n) because a loop is present.
    def arrange_trucks(self):
        # add starting delivery times to each truck
        first_time, second_time, third_time = self.time_convertion()
        self._trucksList[0].add_start_time(first_time)
        self._trucksList[1].add_start_time(second_time)
        self._trucksList[2].add_start_time(third_time)
        self._trucksList[0].add_time_to_delivery_map(first_time)
        self._trucksList[1].add_time_to_delivery_map(second_time)
        self._trucksList[2].add_time_to_delivery_map(third_time)
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

    # This is the base algorithm to optimized the packages for each truck
    # even though there are two loops they are not nested.
    def optimize_delivery(self, current, truck, optimizedTruck):
        if (len(truck.package_list())) == 0:
            return optimizedTruck
        else:
            try:
                lowest_value = 50
                new_location = ''
                for package in truck.package_list():
                    if self.check_distance(current, package.package_address()) < lowest_value:
                        lowest_value = self.check_distance(current, package.package_address())
                        new_location = package.package_address()
                for package in truck.package_list():
                    distance = self.check_distance(current, package.package_address())
                    if distance == lowest_value:
                        optimizedTruck.add_package(package)
                        optimizedTruck.add_distance(distance)
                        truck.remove_package(package)
                        current = new_location
                        self.optimize_delivery(current, truck, optimizedTruck)
            except IndexError:
                pass
            return optimizedTruck

    # Takes from and to addresses and return the distance between them
    # Time-Complexity is O(n) because a loop is present.
    def check_distance(self, fromAddr, toAddr):
        for distances in self._distancesList:
            if (fromAddr in distances.address_from()) and (toAddr in distances.address_to()):
                return float(distances.distance())
            continue

    def set_delivery_time(self, truck):
        current = HUB
        for package in truck.package_list():
            distance = self.check_distance(current,
                                           package.package_address())
            delivered_at = self.time_delivery(truck, distance)
            package.set_package_delivery_time(delivered_at)
            current = package.package_address()

    # Convert times into DateTime format
    # Time-Complexity is O(1)
    def time_convertion(self):
        # the operations below convert the string time into a datetime.timedelta
        (h, m, s) = '8:00:00'.split(':')
        convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        (h, m, s) = '9:10:00'.split(':')
        convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        (h, m, s) = '11:00:00'.split(':')
        convert_third_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        return convert_first_time, convert_second_time, convert_third_time

    def time_delivery(self, truck, distance):
        create_time = distance / SPEED
        distance_min = '{0:02.0f}:{1:02.0f}'.format(*divmod(create_time * 60, 60)) + ':00'
        (h, m, s) = distance_min.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        truck.add_time_to_delivery_map(d)
        sum = datetime.timedelta()
        for times in truck.get_time_map():
            sum += times
        return sum
