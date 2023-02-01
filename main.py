import RPi.GPIO as GPIO
import threading
from motor import * 
from speaker import * 
from button import * 
from led import * 
from time import sleep

#CONSTANTS
POTENTIOMMETER = 0
BUTTON = 0
MOTOR = 0
YELLOW = 17
BLUE = 19
RED = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(27, GPIO.IN)
#GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN)

#main function
if __name__ =="__main__":
    #Welcome
    print("Welcome to horizontally spinning rat")
    motor_hello()

    #Do constant button press checking
    while True:
        if GPIO.input(26) == GPIO.HIGH:
            print("button pressed!")
            led_on(YELLOW)




