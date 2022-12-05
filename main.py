# Brad Pappan, Student ID - 002656581
import csv
import datetime
import packages
import truck
from Hash import HashMap
from distances import load_address_data, load_distance_data, get_distance, get_address

distance_data = []
load_distance_data(distance_data)
my_hash = HashMap()
address_data = []
load_address_data(address_data)


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
        package_order.time += datetime.timedelta(hours=next_address / 18)
        next_package.delivery_time = package_order.time_delivered
        next_package.departure_time = package_order.time_departed


shortest_path(first_truck)
shortest_path(second_truck)
packages.third_truck = min(first_truck, second_truck)
shortest_path(third_truck)


def total_miles():
    return first_truck.mileage + second_truck.mileage + third_truck.mileage


packages.load_package_data('csvFiles/packageFile.csv')


#for i in range(len(my_hash.table)+1):
    #print("Package: {}" .format(my_hash.search(i)))

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
