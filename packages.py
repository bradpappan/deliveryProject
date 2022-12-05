import csv

from main import my_hash


class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, mass, notes, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = status
        self.depart_time = None
        self.delivery_time = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state,
                                                           self.zip_code, self.deadline, self.mass, self.notes,
                                                           self.status, self.delivery_time)


def load_package_data(file_name):
    with open(file_name) as packages:
        package_data = csv.reader(packages, delimiter=',')
        for package in package_data:
            p_id = int(package[0])
            p_address = package[1]
            p_city = package[2]
            p_state = package[3]
            p_zipcode = package[4]
            p_deadline = package[5]
            p_mass = package[6]
            p_notes = package[7]
            p_status = "Currently at the hub"

            p = Package(p_id, p_address, p_city, p_state, p_zipcode, p_deadline, p_mass, p_notes, p_status)

            my_hash.insert(p_id, p)


def current_status(self, convert_time):
    if self.delivery_time < convert_time:
        self.status = "Delivered on time"
    elif self.departure > convert_time:
        self.status = "On its way"
    else:
        self.status = "Currently at the hub"
