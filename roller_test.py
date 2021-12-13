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

while True:
        if GPIO.input(switch) == False:
                print("on")

        if GPIO.input(switch) == True:
                print("off")
        time.sleep(.1)
