# width, length, height
box = [20, 45, 30]

# 0 -> width
# 1 -> length
# 2 -> height

box = {"width": 20, "length": 45, "height": 30}

print(box.get("width"))

box["weight"] = 100

print(box)

box["width"] = 10

print(box)

post_number = {
    "1000": "Ljubljana",
    "8290": "Sevnica",
    "2000": "Maribor"
}

print(post_number.get("1000"))

data = {
    "cities": ["Ljubljana", "Koper"],
    "post_number": [2000, 3000]
}

data = {
    "people": [
        {"name": "Bostjan", "age": 50, "kids":[{"name": "Polde"}, {"name": "Ana"}]},
        {"name": "Peter", "age": 30}
    ],
    "pets": [
        {"name": "Fifi", "age": 3, "type": "dog"}
    ]
}

print(data)

# []
