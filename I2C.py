import smbus
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

b = smbus.SMBus(1)
addr = 0x3A
bus.write_quuick(addr)
b.write_byte_data(addr,0x0F,0x49)
b.write_byte_data(addr,0x12,0xE0)
b.write_byte_data(addr,0x20,0x57)

while True:
	b.write_quick(0x3B)
	x = b.read_byte_data(addr,0x08)
	print "Mag X = ",x

	y = b.read_byte_data(addr,0x0A)
	print "Mag Y = ",y

	z = b.read_byte_data(addr,0x0C)
	print "Mag Z = ",z

	x1 = b.read_byte_data(addr,0x28)
	print "Accl X = ",x1

	y1 = b.read_byte_data(addr,0x2B)
	print "Accl Y = ",y1

	z1 = b.read_byte_data(addr,0x2D)
	print "Accl Z = ",z1
