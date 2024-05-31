import random

print("                      Hauwa Adams kitchen             ")
print("")
print("           Functions of this app:               ")
print("")
print("A. Choosing for hausa traditional food")
print("B. Choosing for snacks")
print("C. Choosing for drinks")
print("D. Exit")
print("")
like = input("Enter the Alphabet name you want: ")


while True:


    if like == "a".lower():
        user_input = input("Should the computer search for hausa traditional food for you? (Yes/No): ")
        traditional_food = ["tuwon shinkafa", "tuwo", "tuwon dawa", "masara", "danbo", "moi moi", "waina", "akara","panki", "shinkafa da miya", "dan waki", "patan waki"]
        traditional_random = random.choice(traditional_food)
        print(traditional_random)
        like = input("Enter the Alphabet name you want: ")

    elif like == "b".lower():
        user_input = input("Should the computer search snacks for you? (Yes/No): ")
        snacks = ["Meat pie", "Fish pie", "Donut", "Chin-Chin", "Bugar", "Shawarma", "Pizza", "Fish roll", "Egg-roll", "Samosa"]
        snacks_random = random.choice(snacks)
        print(snacks_random)
        like = input("Enter the Alphabet name you want: ")

    elif like == "c".lower():
        user_input = input("Should the computer search for drinks for you? (Yes/No): ")
        drinks = ["Multina", "Fanta", "yogurt", "Water", "Sprite", "coco-cola", "Happy Hours", "7UP", "ice-cream", "pap"]
        drinks_random = random.choice(drinks)
        print(drinks_random)
        like = input("Enter the Alphabet name you want: ")

    elif like != "a" or "b" or "c":
        print("Invalid input")
        quit()
    elif like == "d".lower():
        print("Goodbye")
        quit()