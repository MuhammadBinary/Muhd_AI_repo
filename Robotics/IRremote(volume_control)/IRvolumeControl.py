import serial
import pyautogui

arduino = serial.Serial('COM7', 9600)

while True:
    name = arduino.readline()
    name = name.decode('utf').rstrip()
    print(name)
    if name == 'Volume Up':
        pyautogui.press('volumeup')

    elif name == 'Volume Down':
        pyautogui.press('volumedown')
        pyautogui.move()

    elif name == 'Pause':
        pyautogui.press('playpause')

    elif name == 'Next':
        pyautogui.press('nexttrack')

    elif name == 'prev':
        pyautogui.press('prevtrack')



