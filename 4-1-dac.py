import RPi.GPIO as gpio
import sys

gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setup(dac, gpio.OUT)

def binu(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

try:
    while True:

        value = input("Enter value to convert / (Q) to exit: ")
        

        if value == "Q":
            print("Have a good day!")
            sys.exit(0)

        try:
            value = int(value)
        except ValueError:
            print("Try to enter decimal value.")
            continue

        if not 0 <= value < 2 ** 8:
            print("Your value must be in range 0 -", 2 ** 8)
            continue

        gpio.output(dac, binu(value))
        print("{:.3f}".format(value / (2 ** 8) * 3.3))
finally:
    gpio.output(dac, 0)
    gpio.cleanup()