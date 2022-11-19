

class Truck:

    def __init__(self, address, mileage, packages, depart_time):
        self.address = address
        self.mileage = mileage
        self.packages = packages
        self.depart_time = depart_time

    def __str__(self):
        return "%s, %s, %s, %s" % (self.address, self.mileage, self.packages, self.depart_time)
