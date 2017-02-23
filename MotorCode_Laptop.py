import pygame

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

	#Start Motor Code
	
	#Buffer
	if X<=0.1 and X>=-0.1 and Y<=0.1 and Y>=-0.1:
		RF=0
		RB=0
		LF=0
		LB=0
		print "Buffer" ,"RF = " ,RF, "RB = " ,RB ,"LF = " ,LF, "LB = " ,LB

	elif X<=0.1 and X>=-0.1 and Y<=-0.1: #Forward
		RF=(-Y*100)
		RB=(0)
		LF=(-Y*100)
		LB=(0)
		print "Forward","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB

	elif X<=0.1 and X>=-0.1 and Y>=0.1: #Backward
		RF=(0)
		RB=(Y*100)
		LF=(0)
		LB=(Y*100)
		print "Backward","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB

	elif Y<=0.1 and Y>=-0.1 and X>=0.1: #Right
		RF=(0)
		RB=(X*100)
		LF=(X*100)
		LB=(0)
		print "Right","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB

	elif Y<=0.1 and Y>=-0.1 and X<=-0.1: #Left
		RF=(-X*100)
		RB=(0)
		LF=(0)
		LB=(-X*100)
		print "Left","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB

	elif Y<-0.1 and X>0.1: #First Quadrant
		if (-Y)/X>=1: #Right of Forward
			X = -(Y + X)
			RF=((-Y)*100)
			RB=(0)
			LF=(X*100)
			LB=(0)
			print "Right of Forward","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB

		elif (-Y)/X<1: #Up of Right
			Y = X - Y
			RF=(0)
			RB=((Y)*100)
			LF=(X*100)
			LB=(0)
			print "Up of Right","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB

	elif Y<-0.1 and X<-0.1: #Second Quadrant
		if Y/(-X)>=1: #Left of Forward
			X = Y + X
			RF=(Y*100)
			RB=(0)
			LF=(-X*100)
			LB=(0)
			print "Left of Forward","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB

		elif Y/(-X)<1: #Up of Left
			Y = Y + X
			RF=(Y*100)
			RB=(0)
			LF=(0)
			LB=(-X*100)
			print "Up of Left","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB
	
	elif Y>0.1 and X<-0.1: #Third Quadrant
		if Y/(-X)>=1: #Left of Backward
			X = -Y - X
			RF=(0)
			RB=(Y*100)
			LF=(0)
			LB=(-X*100)
			print "Left of Backward","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB

		elif Y/X<1: #Down of Left
			Y = Y + X
			RF=(Y*100)
			RB=(0)
			LF=(0)
			LB=(-X*100)
			print "Down of Left","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB

	elif Y>0.1 and X>0.1: #Fourth Quadrant
		if Y/X>=1: #Right of Backward
			X = X - Y
			RF=(0)
			RB=(Y*100)
			LF=(0)
			LB=(X*100)
			print "Right of Backward","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB

		elif Y/X<1: #Down of Right
			Y = X - Y
			RF=(0)
			RB=(Y*100)
			LF=(X*100)
			LB=(0)
			print "Down of Right","RF = ",RF,"RB = ",RB,"LF = ",LF,"LB = ",LB	

pygame.quit()					
