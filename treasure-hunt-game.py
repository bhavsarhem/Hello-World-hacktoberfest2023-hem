import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def game_over():
    print_slow("Game over! Would you like to play again? (yes/no)")
    play_again = input().lower()
    if play_again == "yes":
        start_game()
    else:
        print_slow("Thanks for playing!")

def treasure_room():
    print_slow("You've entered the treasure room!")
    print_slow("There's a glittering chest in the center of the room.")
    choice = input("Do you want to open it? (yes/no): ").lower()
    if choice == "yes":
        print_slow("Congratulations! You've found the hidden treasure!")
        game_over()
    else:
        print_slow("You leave the treasure room.")
        main_room()

def monster_room():
    print_slow("You've entered the monster room!")
    print_slow("A giant monster appears in front of you!")
    choice = input("Do you want to fight or run? (fight/run): ").lower()
    if choice == "fight":
        print_slow("You bravely fight the monster!")
        print_slow("But it was too strong for you...")
        game_over()
    else:
        print_slow("You run away from the monster and return to the main room.")
        main_room()

def main_room():
    print_slow("You are in a dimly lit room with three doors.")
    print_slow("One door is on the left, one on the right, and one in the center.")
    choice = input("Which door do you want to choose? (left/right/center): ").lower()
    if choice == "left":
        monster_room()
    elif choice == "right":
        treasure_room()
    elif choice == "center":
        print_slow("You open the door and find an empty room.")
        print_slow("You return to the main room.")
        main_room()
    else:
        print_slow("Invalid choice. Please choose a valid door.")
        main_room()

def start_game():
    print_slow("Welcome to the Text-Based Adventure Game!")
    print_slow("You find yourself in a mysterious place.")
    print_slow("Your goal is to find the hidden treasure.")
    print_slow("You can choose different paths to reach your goal, but beware of monsters!")
    main_room()

if __name__ == "__main__":
    start_game()
