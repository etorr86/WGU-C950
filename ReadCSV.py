import csv

# Open CSV File
from HashTable import HashTable


with open('Data/PackageFile.csv') as packageFile:
    readCSV = csv.reader(packageFile, delimiter=',')
    packageHashMap = HashTable()

    # Read values from CSV file and added to the custom hash table, where the key
    # will be the package ID.
    for row in readCSV:
        packageKey = row[0]
        packageAddress = row[1]
        packageCity = row[2]
        packageState = row[3]
        packageZipCode = row[4]
        packageDeliveryTime = row[5]
        packageWeight = row[6]
        packageNotes = row[7]

        packageValues = [packageAddress,
                         packageCity,
                         packageState,
                         packageZipCode,
                         packageDeliveryTime,
                         packageWeight,
                         packageNotes]

        packageHashMap.insert(packageKey, packageValues)

