import csv

# Open CSV File
from HashTable import HashTable
from Packages import Packages

with open('Data/PackageFile.csv') as packageFile:
    readCSV = csv.reader(packageFile, delimiter=',')
    packageHashMap = HashTable()
    packageMap = HashTable()
    deliveryPackage = Packages()

    # Read values from CSV file and added to the custom hash table, where the key
    # will be the package ID.
    for row in readCSV:
        # Set the package object (new way)
        deliveryPackage._packageKey = row[0]
        deliveryPackage._packageAddress = row[1]
        deliveryPackage._packageCity = row[2]
        deliveryPackage._packageState = row[3]
        deliveryPackage._packageZipCode = row[4]
        deliveryPackage._packageDeliveryTime = row[5]
        deliveryPackage._packageWeight = row[6]
        deliveryPackage._packageNotes = row[7]

        # Set the package object (old way)
        packageKey = row[0]
        packageAddress = row[1]
        packageCity = row[2]
        packageState = row[3]
        packageZipCode = row[4]
        packageDeliveryTime = row[5]
        packageWeight = row[6]
        packageNotes = row[7]

        packageList = [deliveryPackage]
        packageValues = [packageKey,
                         packageAddress,
                         packageCity,
                         packageState,
                         packageZipCode,
                         packageDeliveryTime,
                         packageWeight,
                         packageNotes]

        packageHashMap.insert(packageKey, packageValues)
        packageMap.insert(deliveryPackage.package_key(), packageList)

print("Using variables: ", packageHashMap.find('2'))
print("Using own custom package class: ", packageMap.find('2'))

