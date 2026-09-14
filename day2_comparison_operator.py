temperature = 30
if temperature > 30:
    print("It's a hot day")


temperature = 35
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")


temperature != 30
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")



name = input("Enter your name: ")
if len(name)<3:
    print("Name must be at least 3 characters long.")
elif len(name)>50:
    print("Name must be a maximum of 50 characters long.")
else:
    print("Name looks good!")



weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")