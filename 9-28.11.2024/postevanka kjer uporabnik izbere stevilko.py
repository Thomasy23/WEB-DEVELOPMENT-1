while True:
    x = int(input("Vnesi stevilo za katero zelis postevanko."))

    y = int(input("Vnesi stevilo do kod zelis postevanko."))

    for z in range(0, y, x):
        print(z, end=" ")
    print()

    ponovno = input("Ali zelis poskusiti z drugimi stevili? (da/ne):").lower()

    if ponovno != "da":
        print("Hvala, da si uporabil program!")
        break
