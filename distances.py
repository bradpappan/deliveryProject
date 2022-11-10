import csv


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

with open('csvFiles/distanceData.csv') as distanceNumbers:
    distanceCsv = list(csv.reader(distanceNumbers, delimiter=','))

with open('csvFiles/addressData.csv') as addresses:
    addressCsv = list(csv.reader(addresses, delimiter=','))

    def get_distance(row, col, total):
        distance
