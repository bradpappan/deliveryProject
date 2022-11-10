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


def load_package_data(file_name):
    with open(file_name) as packages:
        package_data = csv.reader(packages, delimiter=',')
        next(package_data)
        for package in package_data:
            p_id = int(package[0])
            p_address = package[1]
            p_city = package[2]
            p_state = package[3]
            p_zipcode = package[4]
            p_deadline = package[5]
            p_mass = package[6]
            p_notes = package[7]

            p = Package(p_id, p_address, p_city, p_state, p_zipcode, p_deadline, p_mass, p_notes)
            print(p)

            myHash.insert(p_id, p)


load_package_data('csvFiles/packageFile.csv')
