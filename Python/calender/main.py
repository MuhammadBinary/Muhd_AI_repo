import random
from calendar import calendar

print("               Welcome to Muhammad innovation on programming")
print("")
print("                      functions of this app:                  ")
print("")
print("A. Checking for the year calender")
print("B. Exit")
print("Please just write the alphabet you want")
print("")
like = input("Enter the Alphabet name you want: ")


while True:

    if like == "a".lower():
        user_input = int(input("Enter the year you want to check: "))
        print(calendar(user_input))
        like = input("Enter the Alphabet name you want: ")

    #elif like != "a" or "b":
        #print("Invalid input")
        #quit()

    elif like == "b".lower():
        print("goodbye")
        quit()

#like = input("Did you want to check for any year calender? (yes/no): ")
