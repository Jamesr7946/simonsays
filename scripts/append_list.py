import time
import random
colors = ['R', 'G', 'B', 'Y']
#appends a balue to a list
def append_list():
	n = random.randint(0,3)  
	colors. append(colors[n])  #appends a new random color to list
	color_string = ''. join(colors) #join the colors from the list together
	for i in range(0, len(colors)): #range goes from 0 to length of the list
		print colors[i].lower() #prints it in lowercase
		time.sleep(1)

if __name__ == '__main__':
	try:
		append_list()
	except KeyboardInterrupt:
		print 'Cya later'
