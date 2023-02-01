import RPi.GPIO as GPIO

def button_is_pressed(PIN):
    print("Checking button")
    if GPIO.input(PIN) == GPIO.HIGH: return 1
    else: return 0
