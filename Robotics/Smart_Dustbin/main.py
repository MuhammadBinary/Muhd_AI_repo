import time
import sys
from pymata4 import pymata4

board = pymata4.Pymata4()
triggerpin = 11
echo_pin = 12


def servo(my_board, pin, angle):
    my_board.set_pin_mode_servo(pin)

    # my_board.servo_write(pin, 0)
    # time.sleep(1)
    my_board.servo_write(pin, angle)
    time.sleep(1)


def the_callback(data):
    print(data[2])


board.set_pin_mode_sonar(triggerpin, echo_pin, the_callback)

while True:
    try:
        time.sleep(1)
        dis = board.sonar_read(triggerpin)
        # print(dis)
        if dis <= [40]:
            print("good")
            servo(board, 5, 90)
            time.sleep(1)
        else:
            servo(board, 5, 0)
            time.sleep(1)

    except KeyboardInterrupt:
        board.shutdown()
        sys.exit(0)




