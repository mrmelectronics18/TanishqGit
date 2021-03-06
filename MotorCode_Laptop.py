import pygame

pygame.init()
j=pygame.joystick.Joystick(0)
j.init()

done=False
X=0.0
Y=0.0
X1=0.0
Y1=0.0

while done==False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True

		if event.type == pygame.JOYBUTTONDOWN:
			print("Joystick Button Pressed")
		if event.type == pygame.JOYBUTTONUP:
			print("Joystick Button Released")		

		j.get_numaxes()

		X = j.get_axis(0)
		Y = j.get_axis(1)
		

	#Start Motor Code
	
	#Buffer
	if X<=0.1 and X>=-0.1 and Y<=0.1 and Y>=-0.1: #Buffer
		RF=(0)
		RB=(0)
		LF=(0)
		LB=(0)
		print "Buffer","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB,"X = ",X,"Y = ",Y

	elif X<0.1 and X>-0.1 and Y<-0.1: #Forward
		RF=(-Y*100)
		RB=(0)
		LF=(-Y*100)
		LB=(0)
		print "Forward","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB,"X = ",X,"Y = ",Y

	elif X<0.1 and X>-0.1 and Y>0.1: #Backward
		RF=(0)
		RB=(Y*100)
		LF=(0)
		LB=(Y*100)
		print "Backward","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB,"X = ",X,"Y = ",Y

	elif Y<0.1 and Y>-0.1 and X>0.1: #Right
		RF=(0)
		RB=(X*100)
		LF=(X*100)
		LB=(0)
		print "Right","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB,"X = ",X,"Y = ",Y

	elif Y<0.1 and Y>-0.1 and X<-0.1: #Left
		RF=(-X*100)
		RB=(0)
		LF=(0)
		LB=(-X*100)
		print "Left","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB,"X = ",X,"Y = ",Y

	elif Y<(-0.1) and X>(0.1): #First Quadrant
		Y1 = -Y
		if Y1/X>=1: #Right of Forward
			Y2 = Y1 - X
			RF=((Y2)*100)
			RB=(0)
			LF=((X)*100)
			LB=(0)
			print "Right of Forward","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB," X = ",X," Y = ",Y,"First Quadrant"

		else: #Up of Right
			Y2 = Y1 - X
			RF=(0)
			RB=-(Y2*100)
			LF=((X)*100)
			LB=(0)
			print "Up of Right","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB," X = ",X," Y = ",Y,"First Quadrant"

	elif Y<(-0.1) and X<(-0.1): #Second Quadrant
		X1 = -X
		Y1 = -Y
		if Y1/X1>=1: #Left of Forward
			X2 = X1 - Y1
			RF=((Y1)*100)
			RB=(0)
			LF=-(X2*100)
			LB=(0)
			print "Left of Forward","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB," X = ",X," Y = ",Y,"Second Quadrant"

		else: #Up of Left
			X2 = Y1 - X1
			RF=((Y1)*100)
			RB=(0)
			LF=0
			LB=-(X2*100)
			print "Up of Left","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB," X = ",X," Y = ",Y,"Second Quadrant"

	elif Y>(0.1) and X<(-0.1): #Third Quadrant
		X1 = -X
		if Y/X1>=1: #Left of Backward
			Y2 = Y - X1
			RF=0
			RB=((Y2)*100)
			LF=0
			LB=((X1)*100)
			print "Left of Backward","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB," X = ",X," Y = ",Y,"Third Quadrant"

		else: #Down of Left
			Y2 = Y - X1
			RF=-(Y2*100)
			RB=0
			LF=0
			LB=((X1)*100)
			print "Down of Left","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB," X = ",X," Y = ",Y,"Third Quadrant"

	elif Y>(0.1) and X>(0.1): #Fourth Quadrant
		if Y/X>=1: #Right of Backward
			Y1 = Y - X
			RF=((Y1)*100)
			RB=(0)
			LF=((X)*100)
			LB=(0)
			print "Right of Backward","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB," X = ",X," Y = ",Y,"Fourth Quadrant"

		else: #Down of Right
			Y1 = Y - X
			RF=(0)
			RB=-(X*100)
			LF=((Y1)*100)
			LB=(0)
			print "Down of Right","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB," X = ",X," Y = ",Y,"Fourth Quadrant"

pygame.quit()					
