import random

def promote():
    print("                  Welcome to Muhammad innovation and programming              ")
    print("")
    print("Please don't enter rubbish")
    user_enter = input("what is your over-ral grade: ")


    if user_enter.lower() == "50":
        print("you are promoted to the next class but try next team to pass 50% else you will repeat")
    elif user_enter.lower() > "50":
        print("promoted to the next class")
    elif user_enter.lower() < "50":
        print("Repeated.you can do better next team")

promote()



