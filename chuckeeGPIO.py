import RPi.GPIO as GPIO # Import GPIO library
from time import time, sleep
from random import randint

def button_callback(channel):
    global run
    global stop
    global result
    if run == True:
        run = False
        if stop == 8:
            result = 0
            print("You hit the jackpot!")
            win()
        else:
            result = 1
            print("You lose")
            for i in range(0,5):
                lose()


def game():
    global run
    global stop
    time = 0.04
    run = True
    stop = 0
    while run:
        #increase
        for i in range(0,17):
            if run:
                stop = i
                GPIO.output(led[i],True)
                if i > 0:
                    GPIO.output(led[i-1],False)
                        
                sleep(time)
                
        GPIO.output(led[15],False)
        time = randint(2,4) / 100
            
        #decrease
        for i in range(16,-1,-1):
            if run:
                stop = i
                GPIO.output(led[i],True)
                if i < 16:
                    GPIO.output(led[i+1],False)
                            
                sleep(time)
                
        GPIO.output(led[1],False)
        time = randint(2,4) / 100


def win():
    time = 0.05
    for i in range(0,3):
        for i in range (0, 8):
            GPIO.output(led[i],True)
            GPIO.output(led[16-i],True)
            
            if i > 0:
                GPIO.output(led[i-1],False)
                GPIO.output(led[17-i],False)
                
                sleep(time)

        GPIO.output(led[7],False)
        GPIO.output(led[9],False)
            
        for i in range (7, -1, -1):
            GPIO.output(led[i],True)
            GPIO.output(led[16-i],True)
                
            if i < 7:
                GPIO.output(led[i+1],False)
                GPIO.output(led[15-i],False)
                
                sleep(time)
    
    time = 0.1
    for i in range(0,5):
        GPIO.output(led[0],True)
        GPIO.output(led[8],True)
        GPIO.output(led[16],True)
        sleep(time)
        GPIO.output(led[0],False)
        GPIO.output(led[8],False)
        GPIO.output(led[16],False)
        sleep(time)


def lose():
    time = 0.1
    GPIO.output(led[stop],True)
    sleep(time)
    GPIO.output(led[stop],False)
    sleep(time)


#GPIO setup
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

#LED setup
led = [37, 35, 33, 31, 29, 32, 23, 21, 19, 26, 24, 22, 18, 16, 12, 10, 8]
for i in range(0,17):
    GPIO.setup(led[i], GPIO.OUT)
    GPIO.output(led[i],False) #off

#button setup
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(40,GPIO.RISING,callback=button_callback)


#game
print("Welcome to Chuckee!")

for i in range(1,4):
    #message = input("Attempt #" + str(i))
    stop = 0
    game()
    if result == 0:
        sleep(4)
    else:
        sleep(2)

print("Game Over!")

GPIO.cleanup() # Clean up
