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
#BUZZER = 0
#KNOB = 0
#MOTOR = 0
#YELLOW = 0
#GREEN = 0
#BLUE = 0
#RED = 0

#SETUP
def setup():
    #GPIO settings
    GPIO.setmode(GPIO.BCM)

    #tim TODO
    #GPIO.setup(START_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set in as off when initializing
    GPIO.setup(START_BUTTON, GPIO.IN)

    #mora TODO
    #

    #edgar TODO
    #

    #lara TODO
    #

    #LEDS
    #GPIO.setup(YELLOW, GPIO.OUT)
    #GPIO.setup(BLUE, GPIO.OUT)
    #GPIO.setup(RED, GPIO.IN)
    #GPIO.setup(GREEN, GPIO.IN)

#main function
if __name__ =="__main__":
    #Welcome, and setup
    setup()
    print("Welcome to horizontally spinning rat")
    print("Press the button to begin.")

    #Do constant button press checking
    while True:
        if button_is_pressed(START_BUTTON): #GPIO.input(START_BUTTON) == GPIO.HIGH:
            print("start button pressed!")
        #elif button_is_pressed(STOP_BUTTON): # Sleep for half a second? FIXME
            #print("stop button pressed!")
        #else: 
        sleep(1) #Sleep for a second? FIXME

    #Exit cleanly
    GPIO.cleanup()
