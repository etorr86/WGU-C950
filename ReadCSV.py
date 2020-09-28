import csv
import pandas as pd

# Open CSV File
from Distance import Distance
from HashTable import HashTable
from Packages import Packages


class CSVDataLoader:

    # function that gets call to return a list of package objects into a hash table
    def load_packages(self):
        with open('Data/PackageFile.csv') as packageFile:
            read_package_csv = csv.reader(packageFile, delimiter=',')
            package_map = HashTable()

            # Read values from CSV file, insert the values into the package model
            # insert the package object into the custom hast table.
            for row in read_package_csv:
                delivery_package = Packages(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                package_map.insert(delivery_package.package_key(), delivery_package)

        return package_map

    # function that gets call to return a list of distance objects
    def load_distances(self):
        with open('Data/DistanceFile.csv') as distanceFile:
            location_list = list(csv.reader(distanceFile, delimiter=','))
            # get the location list minus the 1X1 which is not needed
            locations = location_list[0][1:]
            distance_list = []
            counter = 1

            # This will loop over all the records and create a list of distances objects
            # # Space-Time complexity is O(n^2) because nested loop is present.
            for location in locations:
                for row in location_list[:][1:]:
                    distance = Distance(location, row[0], row[counter])
                    distance_list.append(distance)
                counter += 1

        return distance_list
