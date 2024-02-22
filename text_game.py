import time

def intro():
    print("Welcome to Space Adventure!")
    time.sleep(1)
    print("You find yourself on a spaceship.")
    time.sleep(1)
    print("Your mission is to explore the unknown.")
    time.sleep(1)

def choose_action():
    print("\nChoose your action:")
    print("1. Explore the alien planet")
    print("2. Investigate a mysterious signal")
    print("3. Return to Earth")

    choice = input("Enter the number of your choice: ")
    return choice

def explore_planet():
    print("You land on an alien planet.")
    time.sleep(1)
    print("You encounter friendly aliens who offer you advanced technology.")
    time.sleep(1)
    print("What do you do?")
    time.sleep(1)
    print("1. Accept the technology")
    print("2. Politely decline")

    choice = input("Enter the number of your choice: ")
    return choice

def investigate_signal():
    print("You follow the mysterious signal.")
    time.sleep(1)
    print("You discover a hidden space station.")
    time.sleep(1)
    print("What do you do?")
    time.sleep(1)
    print("1. Enter the space station")
    print("2. Ignore the signal and return to your ship")

    choice = input("Enter the number of your choice: ")
    return choice

def main():
    intro()

    while True:
        action_choice = choose_action()

        if action_choice == '1':
            planet_choice = explore_planet()
            if planet_choice == '1':
                print("You accept the advanced technology and continue your journey.")
            elif planet_choice == '2':
                print("You decline and return to your spaceship.")

        elif action_choice == '2':
            signal_choice = investigate_signal()
            if signal_choice == '1':
                print("You enter the space station and uncover valuable information.")
            elif signal_choice == '2':
                print("You decide to ignore the signal and return to your ship.")

        elif action_choice == '3':
            print("You decide to return to Earth. Thanks for playing!")
            break

        else:
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main()
