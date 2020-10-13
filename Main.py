from ReadCSV import CSVDataLoader
from Utils import (SelectedOptions, Templates)
from Delivery import Delivery


def main():
    data_loader = CSVDataLoader()
    wgu_packages = data_loader.load_packages()
    wgu_distances = data_loader.load_distances()
    delivery = Delivery(wgu_distances, 3, wgu_packages)
    delivery.start_delivery()
    Templates.miles_traveled(delivery.get_total_distance())
    # Main point of entry, user will have the options to check status of packages
    Templates.welcome()
    selected_option = int(input(Templates.menu_template()))

    while selected_option != SelectedOptions.exitProgram:
        if selected_option == SelectedOptions.individualPackages:
            try:
                package_id = input(Templates.package_lookup())
                package_time = input(Templates.package_time())
                delivery.get_status_by_package(package_id, package_time)
            except ValueError:
                print('Invalid entry')
                exit()
        elif selected_option == SelectedOptions.getAllPackagesStatus:
            try:
                package_time = input(Templates.package_time())
                delivery.get_status_by_time(package_time)
            except ValueError:
                print('Invalid entry')
                exit()
        elif selected_option == SelectedOptions.exitProgram:
            exit()
        else:
            print("Invalid Value")
            exit()


if __name__ == '__main__':
    main()
