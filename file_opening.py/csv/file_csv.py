import csv

with open("teja.csv","r") as file:
    new = csv.reader(file)

    for row in new:
        print(row)