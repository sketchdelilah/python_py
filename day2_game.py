secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("You failed!")




command = ""
while True: 
    command = input("> ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that.")