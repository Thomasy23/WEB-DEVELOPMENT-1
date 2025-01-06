a = [5, 15, 30, -5]
a.sort()

print(a)

a = [
    {"number": 10, "text": hooray},
    {"number": -5, "text": hooray},
    {"number": -2, "text": hooray}
]

sorted_a = sorted(a, key=lambda x: x["number"])

print(sorted_a)
