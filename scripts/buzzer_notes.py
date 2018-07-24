#this scripts iplays one of the random notes on passifve buzer
import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#buzzer is on pin 32 
buzz_pin = 32
#set passive buzzer pins as output
GPIO.setup(buzz_pin, GPIO.OUT)
Buzz= GPIO.PWM(buzz_pin, 1000)
frequencies = [220, 440, 880, 6000]
counter = 0
while counter<5:
	n = random.randint(0,3)
	Buzz.ChangeFrequency(frequencies[3])
	Buzz.start(50)
	time.sleep(0.5)
	counter = counter + 1
Buzz.stop()
