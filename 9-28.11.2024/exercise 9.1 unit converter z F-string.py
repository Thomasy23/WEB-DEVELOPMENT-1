print("*******Pozdravljen v pretvorniku iz kilometov v milje.*******")
print("")

while True:
    print("Vnesi stevilo kilometrov, ki jih zelis pretvoriti. Vpisi samo stevila!")

    km = input("Kilometri: ")

    km = float(km.replace(",", "."))  # zamenja vejico z piko, ce uporabnik vnese vejico

    miles = km * 0.621371

    print(f"{km} kilometrov je {miles} milj.")

    choice = input("Ali zelis naslednjo pretvorbo (y/n):")

    if choice.lower() != "y" and choice.lower() != "yes":
        break
