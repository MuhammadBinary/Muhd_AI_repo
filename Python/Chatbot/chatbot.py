import openai
import pyttsx3
import speech_recognition as sr

from api_secrets import API_KEY

openai.api_key = API_KEY

engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone(device_index=2)
# print(sr.Microphone.list_microphone_names())


conversation = ""
user_name = "muhammad"

while True:
    print("listening...")
    try:
        user_input = input("type: ")
    except:
        continue

    prompt = user_name + ": " + user_input + "\nBot:"
    conversation += prompt

    response = openai.Completion.create(engine='text-davinci-001', prompt = conversation, max_tokens = 50)
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split("Bot: ", 1)[0]

    conversation += response_str + "\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()
