print("Dobrodosli v igri fizzbuzz!")

end = input("Vnesi stevilo med 1 in 100: ")
end = int(end)  # pretvori niz v stevilo

for num in range(1, end+1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
