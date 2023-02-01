
def check_button(PIN):
    print("Checking button")
    if GPIO.input(PIN) == GPIO.HIGH:
        print("button pressed!")
    sleep(1)

