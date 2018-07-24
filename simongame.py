import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random
GPIO.setwarnings(False)
colors = ['R', 'G', 'B', 'Y']
name = raw_input ("enter ur name")
print 'hi', name , 'enjoy the game press ctrl-c to end'
#appends a balue to a list
#def append_list():
	#n = random.randint(0,3)  
	#colors. append(colors[n])  #appends a new random color to list
	#color_string = ''. join(colors) #join the colors from the list together
	#for i in range(0, len(colors)): #range goes from 0 to length of the list
		#print colors[i].lower() #prints it in lowercase
		#time.sleep(1)
def colorpart():
	R_pin = 11
	G_pin = 12

	B_pin = 13
	LED.setup(R_pin, G_pin, B_pin)
	counter = 0
	while counter ==0:
		n= random.randint(0,3)
		LED.setColor(colors[n])
		time.sleep(0.4)
		counter = counter 
if __name__ == '__main__':
	try:
		colorpart()
	except KeyboardInterrupt:
		print ' Cya lets have fun', name.upper(), ';)'
		LED.noColor() 
		time.sleep(0.5)
		LED.destroy()
