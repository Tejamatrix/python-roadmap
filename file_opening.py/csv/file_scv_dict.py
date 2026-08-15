import csv

with open("teja.csv","r") as file:
    new = csv.DictReader(file)

    for row in new:
        print(row["name"])