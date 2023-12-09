import random

response = input("Would you like to roll the dice? click y if yes and click n if no")

while response.lower() == "y":

    dice_value = random.randint(1, 6)

    if dice_value == 1:
        print("---------")
        print("|       |")
        print("|   •   |")
        print("|       |")
        print("---------")
    elif dice_value == 2:
        print("---------")
        print("| •     |")
        print("|       |")
        print("|     • |")
        print("---------")
    elif dice_value == 3:
        print("---------")
        print("| •     |")
        print("|   •   |")
        print("|     • |")
        print("---------")
    elif dice_value == 4:
        print("---------")
        print("| •   • |")
        print("|       |")
        print("| •   • |")
        print("---------")
    elif dice_value == 5:
        print("---------")
        print("| •   • |")
        print("|   •   |")
        print("| •   • |")
        print("---------")
    elif dice_value == 6:
        print("---------")
        print("| •   • |")
        print("| •   • |")
        print("| •   • |")
        print("---------")


    response = input("Do you want to roll the dice again? (y/n): ")


print("Goodbye!")