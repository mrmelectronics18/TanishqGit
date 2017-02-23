import pygame

pygame.init()
j = pygame.joystick.Joystick(0)
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
pygame.quit()					
