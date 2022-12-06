# Package class
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

    def __repr__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state,
                                                           self.zip_code, self.deadline, self.mass, self.notes,
                                                           self.status, self.delivery_time)

    def current_status(self, time_status):
        #print(time_status)
        if self.delivery_time < time_status:
            self.status = "Delivered on time"

        elif self.depart_time < time_status:
            #print(self.depart_time)
            #print(time_status)
            self.status = "On its way"

        else:
            self.status = "Currently at the hub"
