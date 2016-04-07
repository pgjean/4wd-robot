import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(15, gpio.OUT)
    gpio.setup(16, gpio.OUT)
    gpio.setup(18, gpio.OUT)
    gpio.setup(22, gpio.OUT)

def forward():
    init()
    gpio.output(15, False)
    gpio.output(16, True)
    gpio.output(18, True)
    gpio.output(22, False)
    time.sleep(1)
    gpio.cleanup()
	
def reverse():
    init()
    gpio.output(15, True)
    gpio.output(16, False)
    gpio.output(18, False)
    gpio.output(22, True)
    time.sleep(1)
    gpio.cleanup()

def turn_right():
    init()
    gpio.output(15, False)
    gpio.output(16, True)
    gpio.output(18, False)
    gpio.output(22, True)
    time.sleep(1)
    gpio.cleanup()

def turn_left():
    init()
    gpio.output(15, True)
    gpio.output(16, False
    gpio.output(18, True)
    gpio.output(22, False)
    time.sleep(3)
    gpio.cleanup()

forward()
reverse()
turn_left()
turn_right()
