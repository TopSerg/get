import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(2, GPIO.IN)
a = GPIO.input(2)
GPIO.output(3, a)
time.sleep(10)   
GPIO.cleanup()