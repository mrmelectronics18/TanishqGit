import RPi.GPIO as GPIO
import time
import spidev

GPIO.setmode(GPIO.BOARD)

spi = spi.SpiDev(0)
spi.open(0,0)

while True:
	data = spi.xfer2([0x00])
	print data[0]

	time.sleep(0.1)

	data1 = spi.xfer2([0x1A,0x2B,0x3F])
	write (data1)

	spi.close()

GPIO.cleanup()	