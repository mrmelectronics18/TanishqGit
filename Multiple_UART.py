import serial
import RPi.GPIO as GPIO
import time

ledpin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledpin,GPIO.OUT)
GPIO.setup(8,GPIO.ALT0)
GPIO.setup(10,GPIO.ALT0)

pwmled = GPIO.PWM(ledpin,500)
pwmled.start(0)

ser = Serial.serial(
	port = '/dev/ttyAMA0',
	baudrate = 4800,
	)

x=0

def map(a,in_min,in_max,out_min,out_max):
	return (a-in_min)*(out_max-out_min) / (in_max-in_min)+out_min

print "Serial is open" , str(ser.isOpen())


print "Press 1 to Get INPUT from Arduino"
x = input()

if(x==1):
	ser.write("2")
	x=0

print "Command Sent to Arduino"

y = ser.readline() #y is arduino
ser.close()

time.sleep(0.5)

GPIO.setup(8,GPIO.ALT5)
GPIO.setup(10,GPIO.ALT5)

ser = Serial.serial(
	port = '/dev/ttyAMA1',
	baudrate = 4800,
	)

print "Serial is open" , str(ser.isOpen())


print "Press 1 to Get INPUT from Atmega"
x = input()

if(x==1):
	ser.write("2")
	x=0

print "Command Sent to Atmega"

z = ser.readline() #z is atmega

b = map(z*y,1,81,0,100)

pwmled.ChangeDutyCycle(b)

ser.close()
GPIO.cleanup()
