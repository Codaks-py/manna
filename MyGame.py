import time
import random


def kaabo():
    print("SELF-TEST")
    time.sleep(5)
    print("To start with, ")
    print("This is a guessing game")
    print("you are to guess a possible outcome from tossing a coin...")
    print("Pick from the options (Head/Tail)")
    print()
    print("\tTO PLAY, ENTER A")
    print("\tTO VIEW LOG, ENTER B")



def fiku():
    file = open("Game2.txt", 'a')

    name = input("Enter your name: ")
    print("Welcome ", name)
    outcome = input("Enter possible outcome: ")

    for out in range(2):
        if random.randint(0,1) == 0:
            out = "Head"
        else:
            out = "Tail"

    print("After tossing to coin")
    time.sleep(2)
    print("The outcome = ", out)

    if out == outcome:
        print("You won!")
    else:
        print("You lose!")


    file.write(name + "\n")
    file.write(outcome + "\n")
    file.write(out + "\n")

    file.close()





def log():
    log_file = open("Game2.txt", 'r')

    name = log_file.readline()
    while name != '':
        outcome = log_file.readline()
        out = log_file.readline()


        name = name.rstrip("\n")
        outcome = outcome.rstrip("\n")
        out = out.rstrip("\n")


        print("Name: ", name)
        print("Outcome: ", outcome)
        print("The actual Outcome from the operation: ", out)
        print()

        name = log_file.readline()
    log_file.close()





def game():
    kaabo()

    repeat = 'yes'
    while repeat == 'yes':
        option = input("Enter your option: ")
        if option == "A":
            fiku()
        elif option == "B":
            log()
        else:
            print("Invalid option picked")

        repeat = input("Like to continue, Enter yes, Anything else quits operations. : ")

game()
