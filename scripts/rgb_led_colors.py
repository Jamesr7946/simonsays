import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random
#this scripts blinks one of four colors
colors = ['R', 'G', 'B', 'Y']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)
counter = 0
while counter ==0:
	n= random.randint(0,3)
	LED.setColor(colors[n])
	time.sleep(0.2)
	counter = counter +1
LED.noColor()
time.sleep(0.5)
LED.destroy()
