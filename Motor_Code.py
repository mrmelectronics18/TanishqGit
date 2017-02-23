import pygame
import RPi.GPIO as GPIO

RFpin =
RBpin =
LFpin =
LBpin =

GPIO.setmode (GPIO.BOARD)
GPIO.setup(RF,GPIO.OUT)
GPIO.setup(RB,GPIO.OUT)
GPIO.setup(LF,GPIO.OUT)
GPIO.setup(LB,GPIO.OUT)

RF = GPIO.PWM(RFpin,500)
RB = GPIO.PWM(RBpin,500)
LF = GPIO.PWM(LFpin,500)
LB = GPIO.PWM(LBpin,500)

RF.start(0)
RB.start(0)
LF.start(0)
LB.start(0)

pygame.init()
j=pygame.joystick.Joystick(0)
j.init()

done=False
X=0
Y=0

while done==False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True

		if event.type == pygame.JOYBUTTONDOWN:
			print("Joystick Button Pressed")
		if event.type == pygame.JOYBUTTONUP:
			print("Joystick Button Released")		

		axes = j.get_numaxes()

		X = j.get_axis(0)
		Y = j.get_axis(1)
			
		print "X = ", X
		print "Y = ", Y

	#Start Motor Code
	
	#Buffer
	if X<0.1 and X>-0.1 and Y<0.1 and Y>-0.1:
		RF.ChangeDutyCycle(0)
		RB.ChangeDutyCycle(0)
		LF.ChangeDutyCycle(0)
		LB.ChangeDutyCycle(0)

	if X<0.1 and X>-0.1 and Y<-0.1: #Forward
		RF.ChangeDutyCycle(-Y*100)
		RB.ChangeDutyCycle(0)
		LF.ChangeDutyCycle(-Y*100)
		LB.ChangeDutyCycle(0)

	if X<0.1 and X>-0.1 and Y>0.1: #Backward
		RF.ChangeDutyCycle(0)
		RB.ChangeDutyCycle(Y*100)
		LF.ChangeDutyCycle(0)
		LB.ChangeDutyCycle(Y*100)

	if Y<0.1 and Y>-0.1 and X>0.1: #Right
		RF.ChangeDutyCycle(0)
		RB.ChangeDutyCycle(X*100)
		LF.ChangeDutyCycle(X*100)
		LB.ChangeDutyCycle(0)

	if Y<0.1 and Y>-0.1 and X<-0.1: #Left
		RF.ChangeDutyCycle(-X*100)
		RB.ChangeDutyCycle(0)
		LF.ChangeDutyCycle(0)
		LB.ChangeDutyCycle(-X*100)								
pygame.quit()					
GPIO.cleanup()
