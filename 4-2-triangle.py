import RPi.GPIO as gpio
import time
import sys

gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
rank = 8

max_value = 2 ** rank
period = 0.1

gpio.setup(dac, gpio.OUT)

def binu(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

try:

    while True:

        period = input("Enter value to convert / (Q) to exit: ")
        

        if period == "Q":
            print("Have a good day!")
            sys.exit(0)

        try:
            period = float(period)
        except ValueError:
            print("Try to enter decimal value.")
            sys.exit(1)

        period /= 2 * max_value

        for value in range(max_value):
            gpio.output(dac, binu(value))
            time.sleep(period)

        for value in range(max_value - 1, -1, -1):
            gpio.output(dac, binu(value))
            time.sleep(period)
finally:
    gpio.output(dac, 0)
    gpio.cleanup()

