from gpiozero import Button, LED
from time import time, sleep
from random import randint

btn = Button(21)

while True:
    if btn.wait_for_press() == True:
        print(btn.wait_for_press())
        sleep(1)
