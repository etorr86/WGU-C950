import csv

# Open CSV File
from HashTable import HashTable
from Packages import Packages

with open('Data/PackageFile.csv') as packageFile:
    readCSV = csv.reader(packageFile, delimiter=',')
    packageHashMap = HashTable()
    packageMap = HashTable()

    # Read values from CSV file, insert the values into the package model
    # insert the package object as a list into the custom hast table.
    for row in readCSV:
        deliveryPackage = Packages(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        packageMap.insert(deliveryPackage.package_key(), [deliveryPackage])

