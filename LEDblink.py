from gpiozero import LED
from time import sleep

whiteLED = LED(9)
redLED = LED(10)
yellowLED = LED(22)
greenLED = LED(27)
blueLED = LED(17)

time = 0.25
on = False

while on:
    redLED.off()
    whiteLED.on()
    sleep(time)
    
    whiteLED.off()
    redLED.on()
    sleep(time)

    redLED.off()
    yellowLED.on()
    sleep(time)

    yellowLED.off()
    greenLED.on()
    sleep(time)

    greenLED.off()
    blueLED.on()
    sleep(time)

    blueLED.off()
    greenLED.on()
    sleep(time)

    greenLED.off()
    yellowLED.on()
    sleep(time)

    yellowLED.off()
    redLED.on()
    sleep(time)

whiteLED.off()
redLED.off()
yellowLED.off()
greenLED.off()
blueLED.off()
