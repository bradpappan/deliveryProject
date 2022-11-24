import csv
import datetime
import packages
from Hash import my_hash


def load_distance_data(dis_data):
    with open('csvFiles/distanceData.csv') as pg_csv:
        data = csv.reader(pg_csv, delimiter=',')

        for distance in data:
            dis_data.append(distance)


distance_data = []

load_distance_data(distance_data)
#print(distance_data)

def load_address_data(add_data):
    with open('csvFiles/addressData.csv') as addCsv:
        data = csv.reader(addCsv, delimiter=',')
        for row in data:
            add_data.append(row[2])


address_data = []

load_address_data(address_data)

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


def shortest_path(package_order):
    needs_delivery = []
    index = 0
    for package_id in package_order.packages:
        package = my_hash.search(package_id)
        needs_delivery.append(package)
    package_order.packages.clear()
    while len(needs_delivery) > 0:
        next_address = 3000
        next_package = None
        for package in needs_delivery:
            if get_distance(address_data.index(package_order.address), address_data.index(package.address)) <= next_address:
                _address = get_distance(address_data.index(package_order.address), address_data.index(package.address))
                _package = package
        package_order.packages.append(next_package.package_id)
        needs_delivery.remove(next_package)
        package_order.mileage += next_address
        package_order.address = next_package.address
        package_order.time += datetime.timedelta(hours=next_address / 18)
        next_package.delivery_time = package_order.time_delivered
        next_package.departure_time = package_order.time_departed


shortest_path(packages.first_truck)
shortest_path(packages.second_truck)


packages.third_truck = min(packages.first_truck, packages.second_truck)
shortest_path(packages.third_truck)


