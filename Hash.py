# Hash map

import csv


class HashMap:
    def __init__(self, initial_capacity=40):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def search (self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
            return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])


# add in status, time it left the hub, and time delivered

class Package:
    def __init__(self, packageid, address, city, state, zipcode, deadline, mass, notes):
        self.packageid = packageid
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.mass = mass
        self.notes = notes

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s," % (self.packageid, self.address, self.city, self.state, self.zipcode, self.deadline, self.mass, self.notes)


def loadpackagedata(fileName):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)
        for package in packageData:
            pId = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline = package[5]
            pMass = package[6]
            pNotes = package[7]

            p = Package(pId, pAddress, pCity, pState, pZipcode, pDeadline, pMass, pNotes)
            # print(p)

            myHash.insert(pId, p)
'''
class loadDistanceData(fileName):
    with open(fileName) as distances
        distanceData = csv.reader(distances)
'''

myHash = HashMap()

loadpackagedata('packageFile.csv')

for i in range(len(myHash.table)+1):
    print("Package: {}" .format(myHash.search(i+1)))


def loadDistanceData(disData):
    with open('distanceData.csv') as pgCsv:
        data = csv.reader(pgCsv, delimiter=',')

        for d in data:
            row = []
            for col in d:
                if (col != ''):
                    row.append(float(col))
                else:
                    row.append(None)
            disData.append(row)

distanceData = []

loadDistanceData(distanceData)
print(distanceData)

# Finish adding address to a list, then continue to C in imp steps.