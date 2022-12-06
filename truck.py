# Truck class
class Truck:

    def __init__(self, address, mileage, packages, departure_time):
        self.address = address
        self.mileage = mileage
        self.packages = packages
        self.departure_time = departure_time
        self.time_delivered = departure_time

    def __str__(self):
        return "%s, %s, %s, %s" % (self.address, self.mileage, self.packages, self.departure_time)

    def __repr__(self):
        return "%s, %s, %s, %s" % (self.address, self.mileage, self.packages, self.departure_time)
