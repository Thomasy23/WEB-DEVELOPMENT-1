with open("data.csv", "r") as people_file:
    contents = people_file.readlines()
    for line in contents:
        data = line.split(",")
        print(data)
