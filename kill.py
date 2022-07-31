import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

motor = 18

GPIO.setup(motor, GPIO.OUT)

GPIO.output(motor, GPIO.LOW)
