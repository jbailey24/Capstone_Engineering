from gpiozero import Button

switch = Button(21)

while True:
    if button.is_pressed:
        print('hello')
