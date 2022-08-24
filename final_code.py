# this imports more functions for us to work with
import pygame
from time import time
from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# this assigns certain pins to the pi to control swicthes, the motor, and the red button
switchC = 21
switchD = 26
switchE = 6
switchG = 20

motor = 18
button = 16
shutdown_button = 24

# this is telling the pi how to interpret signals from the pins
GPIO.setup(switchC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switchD, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switchE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switchG, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(motor, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(shutdown_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# this is establishing what audio files from the pi's hard drive will be run with each switch.
# if you want to change the sound that plays as a result of the C switch being pressed, change the Piano_Samples/C.wav to whatever file you'd like to play instead.
# by the way, the files are just C.wav, D.wav, etc, but they're in a folder called Piano_Samples, which we need to tell the pi to go into before it can find those files.
pygame.mixer.init()
C = pygame.mixer.Sound("Piano_Samples/C.wav")
D = pygame.mixer.Sound("Piano_Samples/D.wav")
E = pygame.mixer.Sound("Piano_Samples/E.wav")
G = pygame.mixer.Sound("Piano_Samples/G.wav")


# here's a big one. right here is a function called spin().
# this section here won't actually run this code yet. instead, we're telling the pi, "if we say to run spin(), run this."
def spin():
	# the code is going to loop really fast through checking if the switches are pressed, so fast that it might loop twice while a peg is still pressing a switch down.
	# if that were to happen, it would try to play the audio file twice, but we want it to only play once.
	# with this switch_state stuff, we are going to check every time that a switch is pressed that it is actually a new, separate press, not just the switch being held down.
	switch_stateC = 0 
	previousC = 0
	switch_stateD = 0
	previousD = 0
	switch_stateE = 0
	previousE = 0
	switch_stateG = 0
	previousG = 0
	
	# this next line sets the variable start_time equal to the current time (in seconds since Jan 1 1970).
	# as the code moves forward, the current time will change, but start_time will stay set to what the current time was at the time when we set it.
	# by subtracting the start time from the current time, we can measure how long it has been since we set the start time.
	# this is how we're going to get the motor to run for exactly 16.74 seconds.
	start_time = time()
	current_time = 0

	# this loop is going to run until the current time is more than 16.74 seconds past the time when the disc started spinning.
	while current_time < (start_time + 16.74):
		# if the swithch is on, switch_state is set to 1. If it's off, switch_state is set to 0.
		if GPIO.input(switchC) == False:
			switch_stateC = 1

		if GPIO.input(switchC) == True:
			switch_stateC = 0

		# if the switch is on and was off in the last loop, then we play the file associated with C.
		# earlier, we essentially created a shorthand where whenever we say C, we actually mean Piano_Samples/C.wav.
		# this is because typing all that would be lame.
		if switch_stateC == 1 and switch_stateC != previousC:
			pygame.mixer.Sound.play(C) 
			while pygame.mixer.music.get_busy() == True:
				continue

		# this is the same as the code for checking the C switch, just for the D switch. after this we'll do the same with E and G.
		if GPIO.input(switchD) == False:
			switch_stateD = 1

		if GPIO.input(switchD) == True:
			switch_stateD = 0

		if switch_stateD == 1 and switch_stateD != previousD:
			pygame.mixer.Sound.play(D)
			while pygame.mixer.music.get_busy() == True:
				continue
		# E switch
		if GPIO.input(switchE) == False:
			switch_stateE = 1

		if GPIO.input(switchE) == True:
			switch_stateE = 0

		if switch_stateE == 1 and switch_stateE != previousE:
			pygame.mixer.Sound.play(E)
			while pygame.mixer.music.get_busy() == True:
				continue
		# G switch
		if GPIO.input(switchG) == False:
			switch_stateG = 1

		if GPIO.input(switchG) == True:
			switch_stateG = 0

		if switch_stateG == 1 and switch_stateG != previousG:
			pygame.mixer.Sound.play(G)
			while pygame.mixer.music.get_busy() == True:
				continue

		sleep(.01) # this pauses the code for a hundreth of a second so that the pi doesn't run through code too quickly and get overworked.

		# now we're defining previousC, D, etc. 
		# these values will tell the code in the next loop whether the switches were on or off in the previous loop.
		previousC = switch_stateC
		previousD = switch_stateD
		previousE = switch_stateE
		previousG = switch_stateG

		# this updates the current_time so that it's still accurate.
		current_time = time() 

		
# down here is the actual code that gets looped through constatntly.
# everything else was setting it all up so that the pi knows what to do and how to interpret all the inputs it's about to get.
# now we're gonna actually get those inputs.

while True:
	
	# translation: "if the big red button is pressed,"
	if GPIO.input(button) == False:
		GPIO.output(motor, GPIO.HIGH) # "turn the motor on,"
		sleep(.01)
		spin() # "spin the disc and play sounds accordingly,"
		GPIO.output(motor, GPIO.LOW) # "then turn the motor off."
	
	# translation: "if the small interior button is pressed,"
	if GPIO.input(shutdown_button) == False:
		GPIO.output(motor, GPIO.LOW)	#turn the motor off
		print("shutting down")
		# all of this code down here just shuts down the pi
		command = "/usr/bin/sudo /sbin/shutdown -h now"
    		import subprocess
    		process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    		output = process.communicate()[0]
    		print(output)
	sleep(.01)
