import pygame
from time import time
from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

switch = 21
switch2 = 26
switch3 = 19
switch4 = 20

motor = 18
button = 16

GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(motor, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pygame.mixer.init()
S1 = pygame.mixer.Sound("Piano_Samples/C.wav")
S2 = pygame.mixer.Sound("Piano_Samples/D.wav")
S3 = pygame.mixer.Sound("Piano_Samples/E.wav")
S4 = pygame.mixer.Sound("Piano_Samples/G.wav")

switch_state = 0
previous = 0
switch_state2 = 0
previous2 = 0
switch_state3 = 0
previous3 = 0
switch_state4 = 0
previous4 = 0

def spin():
	
	start_time = time()
	current_time = 0
	
	while current_time < (start_time + 12):
		if GPIO.input(switch) == False:
			switch_state = 1

		if GPIO.input(switch) == True:
			switch_state = 0

		if switch_state == 1 and switch_state != previous:
			print("C")
			#pygame.mixer.stop()
			pygame.mixer.Sound.play(S1)
			while pygame.mixer.music.get_busy() == True:
				continue

		if GPIO.input(switch2) == False:
			switch_state2 = 1

		if GPIO.input(switch2) == True:
			switch_state2 = 0

		if switch_state2 == 1 and switch_state2 != previous2:
			print("D")
			#pygame.mixer.stop()
			pygame.mixer.Sound.play(S2)
			while pygame.mixer.music.get_busy() == True:
				continue

		if GPIO.input(switch3) == False:
			switch_state3 = 1

		if GPIO.input(switch3) == True:
			switch_state3 = 0

		if switch_state3 == 1 and switch_state3 != previous3:
			print("E")
			#pygame.mixer.stop()
			pygame.mixer.Sound.play(S3)
			while pygame.mixer.music.get_busy() == True:
				continue

		if GPIO.input(switch4) == False:
			switch_state4 = 1

		if GPIO.input(switch4) == True:
			switch_state4 = 0

		if switch_state4 == 1 and switch_state4 != previous4:
			print("G")
			#pygame.mixer.stop()
			pygame.mixer.Sound.play(S4)
			while pygame.mixer.music.get_busy() == True:
				continue

		time.sleep(.01)

		previous = switch_state
		previous2 = switch_state2
		previous3 = switch_state3
		previous4 = switch_state4
		
		current_time = time() 

while True:
	if GPIO.input(button) == False:
		GPIO.output(motor, GPIO.HIGH)
		sleep(.01)
		print("on")
		spin()
		GPIO.output(motor, GPIO.LOW)
		print("off")
	time.sleep(.01)
