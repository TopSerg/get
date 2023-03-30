import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def binu(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    left = -1
    right = 256
    while right - left > 1:
        mid = int((left + right)/2)

        value = binu(mid)
        gpio.output(dac, value)

        sleep(0.05)

        compvalue = gpio.input(comp)

        if compvalue == 0:
            right = mid
        else:
            left = mid
    return mid
        

try:
    while True:
        gpio.output(leds, 0)
        i = adc()
        n = int(i*8/256)
        for j in range(n):
            gpio.output(leds[j], 1)
        print(i, binu(i))
        sleep(0.05)
        
finally:
    gpio.output(dac, 0)
    gpio.cleanup()