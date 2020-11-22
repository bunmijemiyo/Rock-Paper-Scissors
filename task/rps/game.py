import random


def rock_paper_scissors():
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")
    files = open("rating.txt", "r", encoding="utf-8")
    points = 0
    for names in files:
        if names.split()[0] == user_name:
            points += int(names.split()[1])
            break
    files.close()
    user_input = input().lower()
    default_choice = "rock,paper,scissors"
    if bool(user_input) is False:
        user_choice = default_choice.split(",")
    else:
        user_choice = user_input.split(",")
    print("Okay, let's start")
    decider = len(user_choice) // 2

    while True:
        new_lis1 = []
        new_lis2 = []
        guess = input().lower()
        random.seed()
        computer_choice = random.choice(user_choice)
        if guess in user_choice:
            if computer_choice == guess:
                print(f"There is a draw ({guess})")
                points += 50
            else:
                position1 = user_choice.index(guess)
                if position1 >= decider:
                    new_lis1.extend(user_choice[(position1 - decider): position1])
                    if computer_choice in new_lis1:
                        print(f"Well done. The computer chose {computer_choice} and failed")
                        points += 100
                    else:
                        print(f"Sorry, but the computer chose {computer_choice}")

                elif position1 < decider:
                    new_lis2.extend(user_choice[(position1 + 1): position1 + decider + 1])
                    if computer_choice in new_lis2:
                        print(f"Sorry, but the computer chose {computer_choice}")
                    else:
                        print(f"Well done. The computer chose {computer_choice} and failed")
                        points += 100

        elif guess == "!exit":
            print("Bye!")
            break
        elif guess == "!rating":
            print(f"Your rating: {points}")
        else:
            print("Invalid input")


rock_paper_scissors()
