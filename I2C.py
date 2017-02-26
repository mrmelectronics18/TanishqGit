import smbus
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
data3 = 0

addr = 0b11010100

b =smbus.SMBus(1)

while True:
	x=b.read_word_data(addr,0b00001100)
	print x
	y=b.read_word_data(addr,0b00001010)
        print y
	z=b.read_word_data(addr,0b00001001)
        print z



	
