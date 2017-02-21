import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
while True:
	import time
	GPIO.output(3,True)
	time.sleep(1)
	GPIO.output(3,False)
	time.sleep(1)

