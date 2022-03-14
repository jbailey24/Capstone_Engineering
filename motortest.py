
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

motor = 17
switch = 19

GPIO.setup(motor, GPIO.OUT)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	if GPIO.input(switch) == True:
		GPIO.output(motor, GPIO.LOW)
		sleep(.01)
		print("off")
	if GPIO.input(switch) == False:
		GPIO.output(motor, GPIO.HIGH)
		sleep(.01)
		print("on")

