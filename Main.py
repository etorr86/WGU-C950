from ReadCSV import CSVDataLoader
from Truck import Truck
from Delivery import Delivery


def main():
    data_loader = CSVDataLoader()
    wgu_packages = data_loader.load_packages()
    wgu_distances = data_loader.load_distances()
    truck1, truck2 = arrange_trucks(wgu_packages)
    delivery = Delivery(wgu_distances, [truck1, truck2])

    # Main point of entry, user will have the options to check status of packages
    print('Welcome to WGUPS package tracking platform')
    print("Please enter one of the following options: ")
    selected_option = input("1) Search Individual Packages by ID"
                            "2) Get Status of all Packages"
                            "3) Select New Time"
                            "4) Exit the Program"
                            "Enter Option: ")


# this function will arrange packages in trucks
# Space-Time complexity is O(n) because loop is present.
def arrange_trucks(packages):
    truck1 = Truck(1)
    truck2 = Truck(2)
    for keyItem in packages.keys():
        if 'Can' in packages.find(keyItem).package_notes():
            truck2.add_package(packages.find(keyItem))
        else:
            truck1.add_package(packages.find(keyItem))

    return truck1, truck2


if __name__ == '__main__':
    main()
