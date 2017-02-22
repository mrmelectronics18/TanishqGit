import time
import RPi.GPIO as GPIO

ledpin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledpin,GPIO.OUT)

PwmLed = GPIO.PWM(ledpin,500)
PwmLed.start(0)

while True:
	for i in range (0,100,5):
		PwmLed.ChangeDutyCycle(i)
		time.sleep(0.1)
	for i in range (100,0,-5):
		PwmLed.ChangeDutyCycle(i)
		time.sleep(0.1)	

GPIO.cleanup()
