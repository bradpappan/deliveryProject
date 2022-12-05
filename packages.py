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
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state,
                                                           self.zip_code, self.deadline, self.mass, self.notes,
                                                           self.status, self.delivery_time)

    def __repr__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state,
                                                           self.zip_code, self.deadline, self.mass, self.notes,
                                                           self.status, self.delivery_time)


def current_status(self, convert_time):
    if self.delivery_time < convert_time:
        self.status = "Delivered on time"
    elif self.departure > convert_time:
        self.status = "On its way"
    else:
        self.status = "Currently at the hub"
