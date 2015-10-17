import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)
i = 0

while i < 100:
    time.sleep(0.05)
    gpio.output(12, gpio.HIGH)
    time.sleep(0.05)
    gpio.output(12, gpio.LOW)
    i += 1
