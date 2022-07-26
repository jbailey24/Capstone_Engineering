import pygame
from time import time
from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

switchC = 21
switchD = 26
switchE = 13
switchG = 20

motor = 18
button = 16

GPIO.setup(switchC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switchD, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switchE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switchG, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(motor, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pygame.mixer.init()
C = pygame.mixer.Sound("Piano_Samples/C.wav")
D = pygame.mixer.Sound("Piano_Samples/D.wav")
E = pygame.mixer.Sound("Piano_Samples/E.wav")
G = pygame.mixer.Sound("Piano_Samples/G.wav")



def spin():

	switch_stateC = 0
	previousC = 0
	switch_stateD = 0
	previousD = 0
	switch_stateE = 0
	previousE = 0
	switch_stateG = 0
	previousG = 0
	
	start_time = time()
	current_time = 0

	while current_time < (start_time + 16.74):
		if GPIO.input(switchC) == False:
			switch_stateC = 1

		if GPIO.input(switchC) == True:
			switch_stateC = 0

		if switch_stateC == 1 and switch_stateC != previousC:
			print("C")
			pygame.mixer.Sound.play(C)
			while pygame.mixer.music.get_busy() == True:
				continue

		if GPIO.input(switchD) == False:
			switch_stateD = 1

		if GPIO.input(switchD) == True:
			switch_stateD = 0

		if switch_stateD == 1 and switch_stateD != previousD:
			print("D")
			pygame.mixer.Sound.play(D)
			while pygame.mixer.music.get_busy() == True:
				continue

		if GPIO.input(switchE) == False:
			switch_stateE = 1

		if GPIO.input(switchE) == True:
			switch_stateE = 0

		if switch_stateE == 1 and switch_stateE != previousE:
			print("E")
			pygame.mixer.Sound.play(E)
			while pygame.mixer.music.get_busy() == True:
				continue

		if GPIO.input(switchG) == False:
			switch_stateG = 1

		if GPIO.input(switchG) == True:
			switch_stateG = 0

		if switch_stateG == 1 and switch_stateG != previousG:
			print("G")
			pygame.mixer.Sound.play(G)
			while pygame.mixer.music.get_busy() == True:
				continue

		sleep(.01)

		previousC = switch_stateC
		previousD = switch_stateD
		previousE = switch_stateE
		previousG = switch_stateG

		current_time = time() 

while True:
	if GPIO.input(button) == False:
		GPIO.output(motor, GPIO.HIGH)
		sleep(.01)
		print("on")
		spin()
		GPIO.output(motor, GPIO.LOW)
		print("off")
	sleep(.01)
