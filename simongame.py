import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
buzz_pin = 32
GPIO.setup(buzz_pin, GPIO.OUT)
Buzz= GPIO.PWM(buzz_pin, 1000)
colors = ['R', 'G', 'B', 'Y']
colorr = []
name = raw_input ("enter ur name")
print 'hi', name , 'enjoy the game press ctrl-c to end'
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)
frequencies = [220, 440, 880, 1760]
frequency_list = []
#def append_list():
	#n = random.randint(0,3)  
	#colors. append(colors[n])  #appends a new random color to list
	#color_string = ''. join(colors) #join the colors from the list together
	#for i in range(0, len(colors)): #range goes from 0 to length of the list
		#print colors[i].lower() #prints it in lowercase
		#time.sleep(1)
def colorpart():
	counter = 0
	while counter ==0:
		n= random.randint(0,3)
		colorr.append(colors[n])
		frequency_list.append(frequencies[n])
		for x in range(0,len(colorr)-1):
			Buzz.ChangeFrequency(frequency_list[x])
			Buzz.start(50)
			LED.setColor(colorr[x])
			time.sleep(0.25)
			Buzz.stop()
			LED.noColor()
			time.sleep(0.5)
		
			
	
				
if __name__ == '__main__':
	try:
		colorpart()
	except KeyboardInterrupt:
		print ' Cya lets have fun', name.upper(), ';)'
		LED.noColor() 
		time.sleep(0.5)
		Buzz.stop()
		LED.destroy()
