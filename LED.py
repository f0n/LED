import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(3, gpio.OUT)
i = 0

while i < 100:
    time.sleep(0.1)
    gpio.output(3, gpio.HIGH)
    time.sleep(0.1)
    gpio.output(3, gpio.LOW)
    i += 1
