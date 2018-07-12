from gpiozero import Button, LED
from time import time, sleep
from random import randint

ledGREEN = LED(2)
ledBLUE = LED(3)
btnBLUE = Button(4)
btnGREEN = Button (17)

ledGREEN.off()
ledBLUE.off()
print("Start!")

def blue():
    ledBLUE.on()
    start = time()
    btnBLUE.wait_for_press()
    end = time()
    ledBLUE.off()
    print("Blue:", end=" ")
    print(end - start)

def green():
    ledGREEN.on()
    start = time()
    btnGREEN.wait_for_press()
    end = time()
    ledGREEN.off()
    print("Green:", end=" ")
    print(end - start)

while True:
    sleep(randint(1,5))
    if randint(1,2) == 1:
        blue()
    else:
        green()
