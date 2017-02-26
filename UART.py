import serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

ser = serial.Serial(
	port = '/dev/ttyAMA0',
	baudrate = 9600)

while True:
	 print "Serial is open" , str(ser.isOpen())

	 print "Now Writing"

	 ser.write("UART is WORKING(Transmit)")

	 print "Now Recieving"

	 x = ser.readline()

	 print "UART is Working(Recieve)" , x

ser.close()
