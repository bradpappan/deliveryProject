import csv
import sys


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

    def get_distance(row, col, total):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[row][col]
        return total + float(distance)

    def current_distance(row, col):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[row][col]
        return float(distance)


first_truck = []
first_truck_index_list = []
second_truck = []
second_truck_index_list = []
third_truck = []
third_truck_index_list = []


def shortest_path(truck_list, truck, current_location):
    if len(list) == 0:
        return list
    else:
        try:
            lowest_number = 100.0
            new_location = 0.0
            for index in truck_list:
                if current_distance(current_location, int(index[1])) <= lowest_number:
                    lowest_number = current_distance(current_location, int(index[1]))
                    new_location = int(index[1])
            for index in truck_list:
                if current_distance(current_location, int(index[1])) == lowest_number:
                    if truck == 1:
                        first_truck.append(index)
                        first_truck_index_list.append(index[1])
                        pop_value = truck_list.index(index)
                        truck_list.pop(pop_value)
                        current_location = new_location
                        shortest_path(truck_list, 1, current_location)
                    elif truck == 2:
                        second_truck.append(index)
                        second_truck_index_list.append(index[1])
                        pop_value = truck_list.index(index)
                        truck_list.pop(pop_value)
                        current_location = new_location
                        shortest_path(truck_list, 2, current_location)
                    elif truck == 3:
                        third_truck.append(index)
                        second_truck_index_list.append(index[1])
                        pop_value = truck_list.index(index)
                        truck_list.pop(pop_value)
                        current_location = new_location
                        shortest_path(truck_list, 3, current_location)
        except IndexError:
            pass


first_truck_index_list.insert(0, '0')
second_truck_index_list.insert(0, '0')
third_truck_index_list.insert(0, '0')


def first_truck_index():
    return first_truck_index_list


def first_truck_list():
    return first_truck


def second_truck_index():
    return second_truck_index_list


def second_truck_list():
    return second_truck


def third_truck_index():
    return third_truck_index_list


def third_truck_list():
    return third_truck
