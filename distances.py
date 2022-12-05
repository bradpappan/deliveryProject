import csv
from main import distance_data


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
