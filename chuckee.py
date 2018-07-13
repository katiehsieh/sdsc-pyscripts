from gpiozero import LED, Button
from time import time, sleep
from random import randint

#define LEDs
"""
led0 = LED(26)
led1 = LED(19)
led2 = LED(13)
led3 = LED(6)
led4 = LED(5)
led5 = LED(12)
led6 = LED(11)
led7 = LED(9)
led8 = LED(10) #middle board19
led9 = LED(7)
led10 = LED(8)
led11 = LED(25)
led12 = LED(24)
led13 = LED(23)
led14 = LED(18)
led15 = LED(15)
led16 = LED(14)
"""

led = [LED(26), LED(19), LED(13), LED(6), LED(5), LED(12), LED(11), LED(9), LED(10), LED(7), LED(8), LED(25), LED(24), LED(23), LED(18), LED(15), LED(14)]

#define button
btn = Button(21)

#variables
time = 0.1
run = True
print(run)

btn.wait_for_press()
print("Start!")

while run:
    #increase
    for i in range(0,16):
        
        #Button
        if btn.wait_for_press() == False:
            print(btn.wait_for_press())
            run = False
        else:
            #LEDs
            led[i].on()
            if i > 0:
                led[i-1].off()
            
        sleep(time)
    
    led[15].off()
    time = randint(3,5) / 100
    
    #decrease
    for i in range(16,0,-1):
       

        #Button
        if btn.wait_for_press() == False:
            print(btn.wait_for_press())
            run = False
        else:
             #LEDs
            led[i].on()
            if i < 16:
                led[i+1].off()
                
        sleep(time)
    
    led[1].off()
    time = randint(3,5) / 100

