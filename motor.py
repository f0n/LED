import RPi.GPIO as gpio
import time


def init():
    gpio.setmode(gpio.BOARD)
    gpio.cleanup()
    gpio.setup(8, gpio.OUT)
    gpio.setup(10, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.cleanup()

def bck(tm):
    gpio.output(8, True)
    gpio.output(10, False)
    gpio.output(11, False)
    gpio.output(13, True)
    time.sleep(tm)
    gpio.cleanup()

def fwd(tm):
    gpio.output(8, False)
    gpio.output(10, True)
    gpio.output(11, True)
    gpio.output(13, False)
    time.sleep(tm)
    gpio.cleanup()
    
def lft(tm):
    gpio.output(8, True)
    gpio.output(10, False)
    gpio.output(11, True)
    gpio.output(13, False)
    time.sleep(tm)
    gpio.cleanup()

def rgt(tm):
    gpio.output(8, False)
    gpio.output(10, True)
    gpio.output(11, True)
    gpio.output(13, False)
    time.sleep(tm)
    gpio.cleanup()
    
init()
while True:
    dxn=raw_input("Which way?")
    if dxn=="f":
        fwd(2)
    elif dxn=="b":
        bck(2)
    elif dxn=="r":
        rgt(2)
    elif dxn=="l":
        lft(2)
    else:
        pass

