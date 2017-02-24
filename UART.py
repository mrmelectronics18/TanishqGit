import Serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

ser = Serial.serial(
	port = '/dev/ttyAMA0',
	baudrate = 9600,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.DATABITS_EIGHTBITS,
	timeout = 1
	)

while True:
	 print "Serial is open" , str(ser.isOpen())

	 print "Now Writing"

	 ser.write("UART is WORKING(Transmit)")

	 print "Now Recieving"

	 x = ser.readline()

	 print "UART is Working(Recieve)" , x

	 ser.close()
