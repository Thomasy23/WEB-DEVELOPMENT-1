with open("csv.csv", "r") as csv_file:
    content = csv_file.read().splitlines()

    for row in content:
        row_data = row.split(",")
        print(f"{row_data[0]} is {row_data[1]} years old and {row_data[2]}")
