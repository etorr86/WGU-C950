from ReadCSV import CSVDataLoader
from Truck import Truck
from Delivery import Delivery


def main():
    data_loader = CSVDataLoader()
    wgu_packages = data_loader.load_packages()
    wgu_distances = data_loader.load_distances()
    delivery = Delivery(wgu_distances, 3, wgu_packages)
    delivery.start_delivery()
    print("Total distance: ", delivery.get_total_distance())
    # Main point of entry, user will have the options to check status of packages
    print('Welcome to WGUPS package tracking platform')
    print("Please enter one of the following options: ")
    selected_option = input("1) Search Individual Packages by ID"
                            "2) Get Status of all Packages"
                            "3) Select New Time"
                            "4) Exit the Program"
                            "Enter Option: ")


if __name__ == '__main__':
    main()
