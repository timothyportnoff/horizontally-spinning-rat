def button_is_pressed(PIN):
    print("Checking button")
    if GPIO.input(PIN) == GPIO.HIGH: return 1
    else: return false
