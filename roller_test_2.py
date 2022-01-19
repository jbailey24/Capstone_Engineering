from gpiozero import Button

switch = Button(21)


def test():
        switch.wait_for_press()
        return 'on'
while True:

        if test() == 'on':
                print('hello')
