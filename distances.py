import csv
import datetime

import truck
from Hash import my_hash


def load_distance_data(dis_data):
    with open('csvFiles/distanceData.csv') as pgCsv:
        data = csv.reader(pgCsv, delimiter=',')

        for d in data:
            row = []
            for col in d:
                if col != '':
                    row.append(float(col))
                else:
                    row.append(None)
            dis_data.append(row)


distance_data = []

load_distance_data(distance_data)
print(distance_data)


def load_address_data(add_data):
    with open('csvFiles/addressData.csv') as addCsv:
        data = csv.reader(addCsv, delimiter=',')

        for d in data:
            row = []
            for col in d:
                if col != '':
                    row.append(col)
                else:
                    row.append(None)
            add_data.append(row)


address_data = []

load_address_data(address_data)
print(address_data)

with open('csvFiles/distanceData.csv') as distance_numbers:
    distance_csv = list(csv.reader(distance_numbers, delimiter=','))

with open('csvFiles/addressData.csv') as addresses:
    address_csv = list(csv.reader(addresses, delimiter=','))

    def _distance(row, col, total):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[row][col]
        return total + float(distance)

    def get_distance(row, column):
        distance = distance_csv[row][column]
        if distance == '':
            distance = distance_csv[row][column]
        return float(distance)

    def get_address(address):
        for row in address_csv:
            if address in row[2]:
                return int(row[0])


def shortest_path(package_order):
    needs_delivery = []
    for package_id in package_order.packages:
        package = my_hash.search(package_id)
        needs_delivery.append(package)
    package_order.packages.clear()

    while len(needs_delivery) > 0:
        _address = 1000
        _package = None

        for package in needs_delivery:
            if get_distance(get_address(package_order.address), get_address(package.address)) <= _address:
                _address = get_distance(get_address(package_order.address), get_address(package.address))
                _package = package
        package_order.packages.append(_package.package_id)
        needs_delivery.remove(_package)
        package_order.mileage += _address
        package_order.address = _package.address
        package_order.time += datetime.timedelta(hours=_address / 18)
        _package.delivery_time = package_order.time_delivered
        _package.departure_time = package_order.time_departed


shortest_path(truck.first_truck)
shortest_path(truck.second_truck)


truck.third_truck = min(truck.first_truck, truck.second_truck)
shortest_path(truck.third_truck)


