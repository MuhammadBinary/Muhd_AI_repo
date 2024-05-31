def add(a, b):
    result = a + b
    print(str(a) + " + " + str(b) + " = " + str(result) + "\n")

def sub(a, b):
    result = a - b
    print(str(a) + " - " + str(b) + " = " + str(result) + "\n")

def mult(a, b):
    result = a * b
    print(str(a) + " + " + str(b) + " = " + str(result) + "\n")

def div(a, b):
    result = a / b
    print(str(a) + " / " + str(b) + " = " + str(result) + "\n")

while True:
    print("A. Addition.")
    print("B. Subtraction.")
    print("C. Multiplication.")
    print("D. Division.")
    print("E.Exit.")
    print(" ")
    Write = input("Write the alphabet of which one you want: ")

    if Write == "a" or Write == "A":
         print("Addition.")
         a = int(input("Enter the first number: "))
         b = int(input("Enter the second number: "))
         add(a, b)

    elif Write == "b" or Write == "B":
         print("Subtraction")
         a = int(input("Enter the first number: "))
         b = int(input("Enter the second number:"))
         sub(a, b)

    elif Write == "c" or Write == "C":
         print("Multiplication.")
         a = int(input("Enter the first number: "))
         b = int(input("Enter the second number: "))
         mult(a, b)

    elif Write == "d" or Write == "D":
         a = int(input("Enter the first number: "))
         b = int(input("Enter the second number: "))
         div(a, b)

    elif Write == "e" or Write == "E":
         print("Program ended")
         quit()