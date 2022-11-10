# Hash map

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

    def search(self, key):
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


myHash = HashMap()

for i in range(len(myHash.table)+1):
    print("Package: {}" .format(myHash.search(i+1)))




# add in status, time it left the hub, and time delivered
# To find the address in the distance data, will need a address lookup function to locate which address is in which column.
# Need to call the address table twice, need a source and the destination. That will be whats plugged into the function.
# Will need to return the column number for address, then return the distanceData, then go back and locate the number in the distance data
# Nearest neighbor and manual loading, put the packages that need delivered early 1st truck
# Put the late packages on truck 2
# Truck 3 gets the rest

