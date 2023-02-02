#import RPi.GPIO as GPIO

def run_motor():
    print("Hello world! This function is supposed to run the motor.")

#these three lines should already be in main, but not sure if they still need to be in motor.py
#Import RPi.GPIO as GPIO
#From time import sleep    
#GPIO.setmode(GPIO.BCM)

#function definition
def run_motor():
  #set pins as outputs
  GPIO.setup(2, GPIO.OUT)
  GPIO.setup(3, GPIO.OUT)
  GPIO.setup(4, GPIO.OUT)

  #to set up the pwm commands
  pwm=GPIO.PWM(4, 100)

  #start Pulse Width Modulation with 0 duty so it doesnt run yet
  pwm.start(0)

  #set direction of motor to forward
  GPIO.output(2, True)
  GPIO.output(3, False)

  #set PWM duty to 23%
  #23% power on motor gives us good rat spins/second
  pwm.ChangeDutyCycle(23)

  #turn on the Enable pin on the LD293D
  GPIO.output(4, True)
  #put code to sleep so motor runs for as long as code is asleep
  #5 seconds for now, likely to change depending on length of song
  sleep(5) 

  #turn enable pin back off
  GPIO.output(4, False)

  #stop the Pulse
  pwm.stop()

  #cleanup all of the GPIO channels.this might interfere with the other parts, not sure
  GPIO.cleanup()
