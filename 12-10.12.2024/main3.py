def calculate_sum_of_cart(cart, name):
    s = 0
    for item in cart:
        s += item

    return s, name, [], 3, 5


sum_of_cart, _, l, _, _ = calculate_sum_of_cart([1, 2, 3, 4], "bostjan")
print(sum_of_cart)
print(l)
