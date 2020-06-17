import csv

with open('county_demographics.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        if row["State"] == "AL":
            print(row["State"])