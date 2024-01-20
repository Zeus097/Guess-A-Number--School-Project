import random

computer_number = random.randint(1, 100)
counter = 0
flag = False
print("\033[1;32m Hi there, you will have only 7 attempts - Good Luck! \n")
while True:
    player_input = input("Guess the number (1-100): ")
    counter += 1
    if counter == 4:
        print("\033[1;31m You have 3 left! \n")
    elif counter == 6:
        print(f"\033[1;31m Last attempt, Good Luck! \n")
    elif counter == 7:
        print("\033[1;31m No more attempts... :( \n")
        try_again = input("\033[1;33m Do you want to play again: [y] -- [n] \n")
        if try_again == "y":
            print("\033[1;32m Welcome back \n")
            counter = 0
            continue
        elif try_again == "n":
            print("See you again...")
            break
        else:
            print("\033[1;31m Invalid input. Bue bue ... \n")
            break
    if not player_input.isdigit():
        print("\033[1;31m Opps... \n")
        print("\033[1;31m Invalid input. Try again... \n")
        counter -= 1
        continue
    player_number = int(player_input)

    if player_number == computer_number:
        print("\033[1;32m You guess it! 💡 \n")
        computer_number = random.randint(101, 350)
        player_choice = input("\033[1;33m Do you want to level up ?: [y] -- [n] \n")
        if player_choice == "y":
            print("\033[1;32m Welcome to the second and final level !! \n")
            print("at this level you have unlimited attempts !! ")
            while True:

                counter = 0

                player_input = input("Guess the number (101-350): ")
                if not player_input.isdigit():
                    print("\033[1;31m Opps... \n")
                    print("\033[1;31m Invalid input. Try again... \n")
                    continue
                player_number = int(player_input)

                if player_number == computer_number:
                    print("\033[1;32m You guess it! 💡 \n")
                    break
                elif player_number > computer_number:
                    print("Too High! ☁️🏔☁️ ")
                else:
                    print("Too Low! 🕳 ")

        if flag:
            break

        elif player_choice == "n":
            print("See you again...")
            break
        else:
            if counter == 0:
                break
            else:
                print("\033[1;31m Invalid input. Bue bue ... \n")
                break
    elif player_number > computer_number:
        print("Too High! ☁️🏔☁️ ")
    else:
        print("Too Low! 🕳 ")

print(f"\033[1;36m *****  Game developed by Vasil, Thank you for playing !  -----    ***** \n")
