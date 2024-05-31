import serial
import time


ser = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)

text = []
print("Running...")
while True:
    line = ser.readline().decode('utf-8')
    if line == "":
        pass
    else:
        try:
            text.append(int(line))
            print(text)
        except:
            if (line[0]) == "A":
                if text == []:
                    pass
                else:
                    text.pop()
                    print(text)

            if (line[0]) == "D":
                if text == []:
                    pass
                else:
                    if text == [1, 2, 3]:
                        print("Correct Password")
                    else:
                        print("Incorrect Password")
