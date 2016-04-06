import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(15, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(22, gpio.OUT)

'move foward'
gpio.output(15, True)
gpio.output(16, False)
gpio.output(18, False)
gpio.output(22, True)
time.sleep(1)

'move backward'
gpio.output(15, False)
gpio.output(16, True)
gpio.output(18, True)
gpio.output(22, False)
time.sleep(1)

'turn right'
gpio.output(15, False)
gpio.output(16, True)
gpio.output(18, False)
gpio.output(22, True)
time.sleep(1)

'turn left'
gpio.output(15, True)
gpio.output(16, False)
gpio.output(18, True)
gpio.output(22, False)
time.sleep(1)

gpio.cleanup() 
