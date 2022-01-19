import time
import RPi.GPIO as GPIO

# Pin definition
switch = 21

# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Use built-in internal pullup resistor so the pin is not floating
# if using a momentary push button without a resistor.
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
switch_state = 0
previous = 0

while True:
        if GPIO.input(switch) == False:
                switch_state = 1

        if GPIO.input(switch) == True:
                switch_state = 0

        if switch_state == 1 and switch_state != previous:
                print('on')

        previous = switch_state
