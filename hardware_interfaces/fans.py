import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH)

GPIO.output(4, GPIO.LOW)
raw_input()
GPIO.cleanup(4)
