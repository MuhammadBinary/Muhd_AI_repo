from pydictionary import pydictionary

dictionary = pydictionary()
while True:
    word = input("Enter a word: ")
    print(dictionary.meaning(word))