import RPi.GPIO as GPIO
import threading
from motor import * 
from speaker import * 
from button import * 
from led import * 
from time import sleep

#CONSTANTS
POTENTIOMMETER = 0
START_BUTTON = 26
STOP_BUTTON = 0
BUZZER = 0
MOTOR = 0
YELLOW = 17
GREEN = 0
BLUE = 19
RED = 0

#SETUP
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(YELLOW, GPIO.OUT)
    GPIO.setup(BLUE, GPIO.OUT)
    GPIO.setup(RED, GPIO.IN)
    GPIO.setup(GREEN, GPIO.IN)

#GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # TODO set in as off when initializing
GPIO.setup(26, GPIO.IN)

#main function
if __name__ =="__main__":
    #Welcome, and setup
    print("Welcome to horizontally spinning rat")
    setup()

    #Do constant button press checking
    while True:
        if button_is_pressed(START_BUTTON) GPIO.input(START_BUTTON) == GPIO.HIGH:
            print("button pressed!")
            led_on(YELLOW)
        else if button_is_pressed(STOP_BUTTON) # Sleep for half a second? FIXME
        else sleep(0.5) # Sleep for half a second? FIXME

    #Exit cleanly
    GPIO.cleanup()




