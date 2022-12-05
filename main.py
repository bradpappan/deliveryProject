# Brad Pappan, Student ID - 002656581
import csv
import datetime
from packages import Package
import truck
from Hash import HashMap


def load_distance_data(dis_data):
    with open('csvFiles/distanceData.csv') as pg_csv:
        data = csv.reader(pg_csv, delimiter=',')

        for distance in data:
            dis_data.append(distance)


def load_address_data(add_data):
    with open('csvFiles/addressData.csv') as addCsv:
        data = csv.reader(addCsv, delimiter=',')
        for row in data:
            add_data.append(row[2])


with open('csvFiles/distanceData.csv') as distance_numbers:
    distance_csv = list(csv.reader(distance_numbers, delimiter=','))

with open('csvFiles/addressData.csv') as addresses:
    address_csv = list(csv.reader(addresses, delimiter=','))


def get_distance(row, column):
    distance = distance_data[row][column]
    if distance == '':
        distance = distance_data[row][column]

    return float(distance)


def get_address(address):
    for row in address_csv:
        if address in row[2]:
            return int(row[0])


def load_package_data(file_name):
    with open(file_name) as all_package_info:
        package_data = csv.reader(all_package_info, delimiter=',')
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


distance_data = []
load_distance_data(distance_data)
my_hash = HashMap()
address_data = []
load_address_data(address_data)
load_package_data('csvFiles/packageFile.csv')
my_hash.display()


first_truck = truck.Truck("4001 South 700 East", 0.0, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40],
                          datetime.timedelta(hours=8))
second_truck = truck.Truck("4001 South 700 East", 0.0, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39],
                           datetime.timedelta(hours=10, minutes=20))
third_truck = truck.Truck("4001 South 700 East", 0.0, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33],
                          datetime.timedelta(hours=9, minutes=5))


def shortest_path(package_order):
    needs_delivery = []
    for package_id in package_order.packages:
        package = my_hash.search(package_id)
        needs_delivery.append(package)
    package_order.packages.clear()
    while len(needs_delivery) > 0:
        next_address = 3000
        next_package = None
        for package in needs_delivery:
            if get_distance(get_address(package_order.address), get_address(package.address)) <= next_address:
                next_address = get_distance(get_address(package_order.address), get_address(package.address))
                next_package = package
        package_order.packages.append(next_package.package_id)
        needs_delivery.remove(next_package)
        package_order.mileage += next_address
        package_order.address = next_package.address
        package_order.time_delivered += datetime.timedelta(hours=next_address / 18)
        next_package.delivery_time = package_order.time_delivered
        next_package.departure_time = package_order.departure_time


shortest_path(first_truck)
shortest_path(second_truck)
third_truck.departure_time = min(first_truck.time_delivered, second_truck.time_delivered)
shortest_path(third_truck)


def total_miles():
    return first_truck.mileage + second_truck.mileage + third_truck.mileage


#for i in range(len(my_hash.table)+1):
#    print("Package: {}" .format(my_hash.search(i)))

print("Parcel Service")
print("Total miles for all three truck delivery routes is: " + total_miles())

program_start = input("Type 'begin' to start the program and display where the packages are by time, or type "
                      "'exit' to quit.")

if program_start == "begin":
    try:
        location_lookup = input("Enter a time to check where a package is using HH:MM:SS format.")
        (hh, mm, ss) = location_lookup.split(":")
        time_conversion = datetime.timedelta(hours=int(hh), minutes=int(mm), seconds=int(ss))

    except ValueError:
        print("Invalid entry")
        exit()
