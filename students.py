with open("students.csv") as file:
    for line in file:
        row = line.strip().split(",")
        print(f"{row[0]} is in {row[1]}")