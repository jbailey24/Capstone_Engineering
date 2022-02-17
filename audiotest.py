import RPi.GPIO as GPIO

switch = 21
switch2 = 26
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

import time
import pygame
pygame.mixer.init()
SW = pygame.mixer.Sound("StarWars3.wav")
CB = pygame.mixer.Sound("D3.wav")

switch_state = 0
previous = 0
switch_state2 = 0
previous2 = 0

while True:

	if GPIO.input(switch) == False:
		switch_state = 1

	if GPIO.input(switch) == True:
		switch_state = 0

	if switch_state == 1 and switch_state != previous:
		print("on")
		pygame.mixer.stop()
		pygame.mixer.Sound.play(SW)
		while pygame.mixer.music.get_busy() == True:
			continue
	if GPIO.input(switch2) == False:
		switch_state2 = 1

	if GPIO.input(switch2) == True:
		switch_state2 = 0

	if switch_state2 == 1 and switch_state2 != previous2:
		print("onbutbetter")
		pygame.mixer.stop()
		pygame.mixer.Sound.play(CB)
		while pygame.mixer.music.get_busy() == True:
			continue
	time.sleep(.01)

	previous = switch_state
	previous2 = switch_state2
