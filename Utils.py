from enum import (IntEnum, Enum)


class SelectedOptions(IntEnum):
    individualPackages = 1
    getAllPackagesStatus = 2
    exitProgram = 3


class TruckStatus(str, Enum):
    atHub = "At Hub"
    inTransit = "In Transit"
    delivered = "Delivered At"


class StatusKeyWord(str, Enum):
    left = "Left at"
    leaves = "Leaves at"


class Templates:

    @staticmethod
    def welcome():
        print('Welcome to WGUPS package tracking platform')

    @staticmethod
    def miles_traveled(totalDistance):
        print("Total distance traveled: ", totalDistance)

    @staticmethod
    def menu_template():
        menu = """Please enter one of the following options: 
                   1) Search Individual Packages by ID"
                  "2) Get Status of all Packages"
                  "3) Exit the Program"
                  "Enter Option: """
        return menu

    @staticmethod
    def package_status(package, startTime, keyword):
        if package.status() != TruckStatus.delivered:
            status = f"Package ID: {package.package_key()}, Address: {package.full_address()}, " \
                     f"Required delivery time: {package.package_delivery_time()}, " \
                     f"Package Weight: {package.package_weight()}, Truck Status: " \
                     f" {keyword} {startTime}, Delivery Status: {package.status().value}"
            return status
        else:
            status = f"Package ID: {package.package_key()}, Address: {package.full_address()}, " \
                     f"Required delivery time: {package.package_delivery_time()}, " \
                     f"Package Weight: {package.package_weight()}, Truck Status: " \
                     f" {keyword} {startTime}, Delivery Status: {package.status().value} at {package.delivered_at()}"
            return status

    @staticmethod
    def package_lookup():
        lookup = "Please enter a package ID to lookup: "
        return lookup

    @staticmethod
    def package_time():
        package_time = "Please enter a time in the HH:MM:SS format: "
        return package_time
