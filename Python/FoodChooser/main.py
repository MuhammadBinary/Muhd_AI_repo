import random

def chooser():
    print("       Hauwa Adams kitchen       ")
    user_input = input("did you want to choose food? yes/no: ")
    option = ["rice and stew", "tuwo", "moi moi", "jollof rice", "rice and pepper", ""]

    if user_input == "yes".lower():
        computer_input = random.choice(option)
        print(computer_input)

chooser()