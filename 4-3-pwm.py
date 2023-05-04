import RPi.GPIO as gpio
import sys

FREQUENCY   = 1000
MAX_VOLTAGE = 3.3
STEP        = 0.01

OUTPUT_PIN = 14
dac  = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode(gpio.BCM)
gpio.setup(dac,        gpio.OUT)
gpio.setup(OUTPUT_PIN, gpio.OUT)

pwm = gpio.PWM(OUTPUT_PIN, FREQUENCY)
pwm.start(0)

try:
    while True:
        duty_cycle = input("Please enter duty cycle: ")

        if duty_cycle == 'Q':
            print("Have a good day!")
            sys.exit(0)

        try:
            duty_cycle = float(duty_cycle)
        except ValueError:
            print("Try to enter floating value.")
            continue

        pwm.ChangeDutyCycle(duty_cycle)
        
        print("{:.2f}".format(duty_cycle * MAX_VOLTAGE * STEP))

finally:
    gpio.output(dac,        0)
    gpio.output(OUTPUT_PIN, 0)
    gpio.cleanup()