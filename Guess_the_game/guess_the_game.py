import random

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number (1-100): ")
    if not player_input.isdigit():
        print("Learn to read ! .. and try again with a number!")
        continue

    player_number = int(player_input)

    if player_number == computer_number:
        print("YEEEES YOU WON!")
        break

    elif player_number > computer_number:
        print("Try to go lower!")

    else:
        print("Try to go higher!")
