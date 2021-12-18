import csv

dataset_1 = []
dataset_2 = []

with open('dataset_1.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_1.append(row)

with open('dataset_2_sorted.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_2.append(row)

header1 = dataset_1[0]
planet_data1 = dataset_1[1:]

header2 = dataset_2[0]
planet_data2 = dataset_2[1:]

header = header1 + header2

planet_data = []

for index, datarow in enumerate(planet_data1):
    planet_data.append(planet_data1[index] + planet_data2[index])

with open ('final.csv', 'a+') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerows(planet_data)
