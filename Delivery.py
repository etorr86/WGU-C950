from Truck import Truck
from Utils import (TruckStatus, StatusKeyWord, Templates, time_conversion)
import datetime

HUB = "4001 South 700 East"
SPEED = 18


class Delivery:

    def __init__(self, distances, trucks, packages):
        self._distancesList = distances
        self._trucksList = [Truck() for truck in range(trucks)]
        self._optimizedTruckList = []
        self._packageList = packages
        self._optimizedTruckDict = {}

    # Using the time it will loop and get the status of all packages.
    # Time-Complexity is O(n) because a loop is present.
    def get_status_by_time(self, time):
        convert_user_time = time_conversion(time)
        for key in self._packageList.keys():
            package = self._packageList.find(key)
            delivered_time = package.delivered_at()
            started_time = self._optimizedTruckDict.get(package.get_truck_id()).truck_start_time()
            print(self.get_status(package, started_time, convert_user_time, delivered_time))

    # Using the package and time it will get the status of a single packages.
    # Time-Complexity is O(1).
    def get_status_by_package(self, package, time):
        package_selected = self._packageList.find(package)
        delivered_time = package_selected.delivered_at()
        started_time = self._optimizedTruckDict.get(package_selected.get_truck_id()).truck_start_time()
        convert_user_time = time_conversion(time)
        print(self.get_status(package_selected, started_time, convert_user_time, delivered_time))

    # Main status function, this function gets called by the two previous ones.
    # Time-Complexity is O(1).
    def get_status(self, package, started_time, convert_user_time, delivered_time):
        if started_time >= convert_user_time:
            package.set_status(TruckStatus.atHub)
            return Templates.package_status(package, started_time, StatusKeyWord.leaves)
        elif started_time <= convert_user_time:
            if convert_user_time < delivered_time:
                package.set_status(TruckStatus.inTransit)
                return Templates.package_status(package, started_time, StatusKeyWord.left)
            else:
                package.set_status(TruckStatus.delivered)
                return Templates.package_status(package, started_time, StatusKeyWord.left)

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
            self._optimizedTruckDict[truck.truck()] = ready_truck

        # call function to put times for each package delivered
        for truck in self._optimizedTruckList:
            self.set_delivery_time(truck)

    # Algorithm to arrange trucks and set the times to start delivering packages
    # Time-Complexity is O(n) because a loop is present.
    def arrange_trucks(self):
        # add starting delivery times to each truck
        truck_times = time_conversion(['8:00:00', '9:10:00', '11:00:00'])
        self._trucksList[0].add_start_time(truck_times[0])
        self._trucksList[1].add_start_time(truck_times[1])
        self._trucksList[2].add_start_time(truck_times[2])
        self._trucksList[0].add_time_to_delivery_map(truck_times[0])
        self._trucksList[1].add_time_to_delivery_map(truck_times[1])
        self._trucksList[2].add_time_to_delivery_map(truck_times[2])

        for keyItem in self._packageList.keys():
            if 'EOD' in self._packageList.find(keyItem).package_delivery_time() and len(
                    self._trucksList[2].package_list()) < 16 and 'Can' not in self._packageList.find(
                    keyItem).package_notes() and keyItem != '19':
                if 'Wrong' in self._packageList.find(keyItem).package_notes():
                    wrong_addr_package = self._packageList.find(keyItem)
                    wrong_addr_package.set_package_addr('410 S State St')
                    wrong_addr_package.set_package_city('Salt Lake City')
                    wrong_addr_package.set_package_state('UT')
                    wrong_addr_package.set_package_zip('84111')
                    self._trucksList[2].add_package(self._packageList.find(keyItem))
                else:
                    self._trucksList[2].add_package(self._packageList.find(keyItem))
            elif 'Delayed' in self._packageList.find(keyItem).package_notes():
                self._trucksList[1].add_package(self._packageList.find(keyItem))
            elif 'Can' in self._packageList.find(keyItem).package_notes():
                self._trucksList[1].add_package(self._packageList.find(keyItem))
            elif '10' in self._packageList.find(keyItem).package_delivery_time() and len(
                    self._trucksList[0].package_list()) < 16:
                self._trucksList[0].add_package(self._packageList.find(keyItem))
            elif '10' in self._packageList.find(keyItem).package_delivery_time() and len(
                    self._trucksList[1].package_list()) < 16:
                self._trucksList[1].add_package(self._packageList.find(keyItem))
            elif '9' in self._packageList.find(keyItem).package_delivery_time() and len(
                    self._trucksList[0].package_list()) < 16:
                self._trucksList[0].add_package(self._packageList.find(keyItem))
            elif len(self._trucksList[0].package_list()) < 16:
                self._trucksList[0].add_package(self._packageList.find(keyItem))
            elif len(self._trucksList[2].package_list()) < 16:
                self._trucksList[2].add_package(self._packageList.find(keyItem))
            else:
                self._trucksList[1].add_package(self._packageList.find(keyItem))

    # This is the base algorithm to optimized the packages for each truck
    # even though there are two loops they are not nested, so the time complexity is O(n)
    # for more information refer to the documentation.
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
                    package.set_truck_id(truck.truck())
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

    # Set the delivery times for each package
    # Time-Complexity is O(n) because a loop is present.
    def set_delivery_time(self, truck):
        current = HUB
        for package in truck.package_list():
            distance = self.check_distance(current,
                                           package.package_address())
            delivered_at = self.time_delivery(truck, distance)
            package.set_package_delivery_time(delivered_at)
            current = package.package_address()

    # Do the necessary calculations to get the delivery time from the distance and speed.
    # Time-Complexity is O(n) because a loop is present.
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
