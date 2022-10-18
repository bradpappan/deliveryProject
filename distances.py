import csv


def loadDistanceData(disData):
    with open('csvFiles/distanceData.csv') as pgCsv:
        data = csv.reader(pgCsv, delimiter=',')

        for d in data:
            row = []
            for col in d:
                if col != '':
                    row.append(float(col))
                else:
                    row.append(None)
            disData.append(row)


distanceData = []

loadDistanceData(distanceData)
print(distanceData)


def loadAddressData(addData):
    with open('csvFiles/addressData.csv') as addCsv:
        data = csv.reader(addCsv, delimiter=',')

        for d in data:
            row = []
            for col in d:
                if col != '':
                    row.append(col)
                else:
                    row.append(None)
            addData.append(row)


addressData = []

loadAddressData(addressData)
print(addressData)
