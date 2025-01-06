a = 5
b = 5.4

c = "Somting I am trying to say? :)"

d = True

e = None

list_smartninja = [1, 5, -10, 15, 0, 6, 0, 0, 1]
print(list_smartninja)

mixed_list = [5, "Smart", ":)", 10.5, True, False, None, a, b]
print(mixed_list)

# DATA STRUCTURES -> LIST

list_smartninja.append(10)

print(list_smartninja)

last_element = list_smartninja.pop()

print(last_element)
print(list_smartninja)

first_element = list_smartninja.pop(0)
print(first_element)
print(list_smartninja)

print("Sorting list in ascending order:")
list_smartninja.sort()
print(list_smartninja)
print("Sorting list in descending order:")
list_smartninja.sort(reverse=True)
print(list_smartninja)

for number in list_smartninja:
    print(number)

print("--------")
element = list_smartninja[1]
print(element)
print(list_smartninja)
