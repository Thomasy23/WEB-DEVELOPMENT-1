"""
1. Write a function that two number together and return the sum.

INPUT: a (number), b(number)
OUTPUT: sum -> a + b

2. Write a function that return a cube of a number.

INPUT: a (number)
OUTPUT: b -> cube of a

3. Write a function that does this:
INPUT: Any number + power
OUTPUT: Number to the power

3, 10 -> 3 * 3 * 3... 10x
2, 8 -> 2 * 2 * 2 ... 8x

4. Steps counter

create a function that calculates the number of steps that you make for a certain distance.

Input:
    1. Distance we walked
    2. Length of step
Output:
    Number of steps.
"""

# floor, round

# V funkciji lahko naredis '-> int' in vrne tudi stevilko.


def steps_counter(distance: int, length_of_step: int) -> int:

    return int(distance/length_of_step)


print(steps_counter(1000, 3))


def custom_power_number_loop(a, exp):
    power = a
    for i in range(exp-1):
        power = power * a
    return power


p = custom_power_number_loop(2, 3)
print(p)


"""
Namesto zgornje funkcije lahko uporabimo
pythonovo osnovno matematicno funkcijo POW
in dobimo enak rezultat z manj dela.
"""
p2 = pow(2, 3)
print(p2)


def sum_of_number(a, b):
    return a + b


c = sum_of_number(3, 5)
print(c)


def cube_of_number(a):
    return a * a * a


d = cube_of_number(3)
print(d)


# output of more than one value
def get_square_cube(num):
    square = num * num
    cube = num * num * num

    return square, cube


square_two, cube_two = get_square_cube(2)
print(square_two)
print(cube_two)


# Absolute difference between two number
def absolute_difference(x, y):
    if x > y:
        return x - y
    else:
        return y - x


print(absolute_difference(5, 3))
print(absolute_difference(3, 5))
print(absolute_difference(-5, 3))
print(absolute_difference(-5, -3))
