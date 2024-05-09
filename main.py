import csv

with open("ipl_point_table.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}   

    for row in reader:
        Points = row["PTS"]
        if Points in counts:
            counts[Points] += 1
        else:
            counts[Points] = 1

for Points in counts:
    print(f"{Points}: {counts[Points]}")
