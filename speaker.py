import RPi.GPIO as GPIO
import time

Buzzer = 17
#     0   C    D    E    F    G    A    A#   B
CH = [1, 525, 589, 661, 700, 786, 882, 932, 990]        # Frequency of High C notes
#     0   1    2    3    4    5    6    7    8

song = [
CH[5], CH[2], 
CH[4], CH[5], CH[5], CH[5], CH[4], CH[2], 
CH[4], CH[5], CH[4], CH[2], CH[5], CH[4], CH[2], 
CH[5], CH[5], CH[7], CH[5], CH[7], CH[5], 
CH[5], CH[7], CH[5], CH[5], CH[5], CH[2], 
CH[4], CH[5], CH[4], CH[2], CH[5], CH[4], CH[2], 
CH[5], CH[5], CH[5], CH[5], CH[5], CH[5]
]

beat = [
    0.5, 0.5,
    0.5, 0.5, 1, 1, 0.5, 0.5, 
    0.5, 0.5, 0.5, 1, 0.5, 0.5, 
    0.5, 1, 0.5, 1, 0.5, 0.5, 
    0.5, 0.5, 1, 1, 0.5, 0.5, 
    0.5, 0.5, 1, 1, 0.5, 0.5, 
    0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 
    
    0.5, 1, 0.5, 1, 0.5, 0.5
    ]

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Buzzer, GPIO.OUT)
    global Buzz

def loop():
    while True:
        print ('\n    Playing song...')
        for i in range(1, len(song)):
            if  song[i] == 1 :
                time.sleep(beat[i] *0.25)
            else:
                Buzz = GPIO.PWM(Buzzer, song[i])
                Buzz.start(50)
                time.sleep(beat[i] * 0.25)
                Buzz.stop()
        time.sleep(1)             # Wait a second for next song.

def stop_buzz():
    Buzz.stop()
    GPIO.output(Buzzer, LOW)

def destory():
    Buzz.stop()
    GPIO.output(Buzzer, LOW)
    GPIO.cleanup()

if __name__ == '__main__':        # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:     # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destory()
