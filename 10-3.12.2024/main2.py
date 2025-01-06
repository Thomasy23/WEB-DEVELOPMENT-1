with open("hello.txt", "r") as file:
    contents = file.read().splitlines()

for line in contents:
    print(line)

with open("output.txt", "w") as file:
    file.write("I am outputting here!")
    