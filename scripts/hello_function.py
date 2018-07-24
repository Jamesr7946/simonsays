import time
#this shows  the script for try:except stucture
def loop():
	while True:
		print "hello world"
		time.sleep(5)

if __name__ == '__main__' :
	try:
		loop()
	except KeyboardInterrupt:
		print 'cya later'
