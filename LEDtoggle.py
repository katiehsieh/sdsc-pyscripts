from gpiozero import LED
from time import sleep

redLED = LED(10)
yellowLED = LED(22)
greenLED = LED(27)
blueLED = LED(17)

redLED.blink(0.1,0.2)
redLED.toggle()
sleep(1)
redLED.blink(0.2,0.1)
redLED.toggle()
sleep(1)

#toggle on and off
