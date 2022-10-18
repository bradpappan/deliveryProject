import csv

from Hash import myHash


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
            print(p)

            myHash.insert(pId, p)


loadpackagedata('csvFiles/packageFile.csv')
