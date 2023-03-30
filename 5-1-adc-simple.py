import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def binu(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    for i in range(256):
        value = binu(i)
        gpio.output(dac, value)
        sleep(0.005)
        compvalue = gpio.input(comp)
        if compvalue == 0:
            return i

try:
    while True:
        i = adc()
        print(i, binu(i))
finally:
    gpio.output(dac, 0)
    gpio. cleanup()