'''
Names: Cristian Avalos, Hariharan Sivakumar
Class: CSCE-462
Date Began: 1/18/2021
lab01 - traffic light
'''
# import statements
import RPi.GPIO as GPIO
from time import sleep
import sys
import signal

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Pin variables so that they can easily be changed
# led 1
led1RedPin = 18
led1GreenPin = 23
led1BluePin = 24
# led 2
led2RedPin = 17
led2GreenPin = 27
led2BluePin = 22
# button
buttonPin = 1
# 7 segment display
segmentAPin = 6
segmentBPin = 5
SegmentCPin = 12
segmentDPin = 16
segmentEPin = 20
segmentFPin = 13
segmentGPin = 19

# Class declarations
# Class for LED #1
class led1:
    def __init__(self, red, redPin, green, greenPin, blue, bluePin):
        self.red = red
        self.redPin = redPin
        self.blue = blue
        self.bluePin = bluePin
        self.green = green
        self.greenPin = greenPin
    
    def turnRed(self):
        GPIO.output(self.redPin,1)
        GPIO.output(self.greenPin,0)
        GPIO.output(self.bluePin,0)
        
    def turnGreen(self):
        GPIO.output(self.redPin,0)
        GPIO.output(self.greenPin,1)
        GPIO.output(self.bluePin,0)
        
    def turnBlue(self):
        GPIO.output(self.redPin,0)
        GPIO.output(self.greenPin,0)
        GPIO.output(self.bluePin,1)

    def turnOff(self):
        GPIO.output(self.redPin,0)
        GPIO.output(self.greenPin,0)
        GPIO.output(self.bluePin,0)

class led2:
    def __init__(self, red, redPin, green, greenPin, blue, bluePin):
        self.red = red
        self.redPin = redPin
        self.blue = blue
        self.bluePin = bluePin
        self.green = green
        self.greenPin = greenPin

    def turnRed(self):
        GPIO.output(self.redPin,1)
        GPIO.output(self.greenPin,0)
        GPIO.output(self.bluePin,0)
        
    def turnGreen(self):
        GPIO.output(self.redPin,0)
        GPIO.output(self.greenPin,1)
        GPIO.output(self.bluePin,0)
        
    def turnBlue(self):
        GPIO.output(self.redPin,0)
        GPIO.output(self.greenPin,0)
        GPIO.output(self.bluePin,1)

    def turnOff(self):
        GPIO.output(self.redPin,0)
        GPIO.output(self.greenPin,0)
        GPIO.output(self.bluePin,0)

class segment:
    def __init__(self, a, aPin, b, bPin, c, cPin, d, dPin, e, ePin, f, fPin, g, gPin):
        self.a = a
        self.aPin = aPin
        self.b = b
        self.bPin = bPin
        self.c = c
        self.cPin = cPin
        self.d = d
        self.dPin = dPin
        self.e = e
        self.ePin = ePin
        self.f = f
        self.fPin = fPin
        self.g = g
        self.gPin = gPin

    def display(self, number):
        if (number == 9):
            GPIO.output(self.aPin,1) #a
            GPIO.output(self.bPin,1) #b
            GPIO.output(self.cPin,1) #c
            GPIO.output(self.dPin,1) #d
            GPIO.output(self.ePin,0) #e
            GPIO.output(self.fPin,1) #f 
            GPIO.output(self.gPin,1) #g
        elif (number == 8):
            GPIO.output(self.aPin,1) #a
            GPIO.output(self.bPin,1) #b
            GPIO.output(self.cPin,1) #c
            GPIO.output(self.dPin,1) #d
            GPIO.output(self.ePin,1) #e
            GPIO.output(self.fPin,1) #f 
            GPIO.output(self.gPin,1) #g
        elif (number == 7):
            GPIO.output(self.aPin,1) #a
            GPIO.output(self.bPin,1) #b
            GPIO.output(self.cPin,1) #c
            GPIO.output(self.dPin,0) #d
            GPIO.output(self.ePin,0) #e
            GPIO.output(self.fPin,0) #f 
            GPIO.output(self.gPin,0) #g
        elif (number == 6):
            GPIO.output(self.aPin,1) #a
            GPIO.output(self.bPin,0) #b
            GPIO.output(self.cPin,1) #c
            GPIO.output(self.dPin,1) #d
            GPIO.output(self.ePin,1) #e
            GPIO.output(self.fPin,1) #f 
            GPIO.output(self.gPin,1) #g
        elif (number == 5):
            GPIO.output(self.aPin,1) #a
            GPIO.output(self.bPin,0) #b
            GPIO.output(self.cPin,1) #c
            GPIO.output(self.dPin,1) #d
            GPIO.output(self.ePin,0) #e
            GPIO.output(self.fPin,1) #f 
            GPIO.output(self.gPin,1) #g
        elif (number == 4):
            GPIO.output(self.aPin,0) #a
            GPIO.output(self.bPin,1) #b
            GPIO.output(self.cPin,1) #c
            GPIO.output(self.dPin,1) #d
            GPIO.output(self.ePin,0) #e
            GPIO.output(self.fPin,1) #f 
            GPIO.output(self.gPin,1) #g
        elif (number == 3):
            GPIO.output(self.aPin,1) #a
            GPIO.output(self.bPin,1) #b
            GPIO.output(self.cPin,1) #c
            GPIO.output(self.dPin,1) #d
            GPIO.output(self.ePin,0) #e
            GPIO.output(self.fPin,0) #f 
            GPIO.output(self.gPin,1) #g
        elif (number == 2):
            GPIO.output(self.aPin,1) #a
            GPIO.output(self.bPin,1) #b
            GPIO.output(self.cPin,0) #c
            GPIO.output(self.dPin,1) #d
            GPIO.output(self.ePin,1) #e
            GPIO.output(self.fPin,0) #f 
            GPIO.output(self.gPin,1) #g
        elif (number == 1):
            GPIO.output(self.aPin,0) #a
            GPIO.output(self.bPin,1) #b
            GPIO.output(self.cPin,1) #c
            GPIO.output(self.dPin,0) #d
            GPIO.output(self.ePin,0) #e
            GPIO.output(self.fPin,0) #f 
            GPIO.output(self.gPin,0) #g
        elif (number == 0):
            GPIO.output(self.aPin,1) #a
            GPIO.output(self.bPin,1) #b
            GPIO.output(self.cPin,1) #c
            GPIO.output(self.dPin,1) #d
            GPIO.output(self.ePin,1) #e
            GPIO.output(self.fPin,1) #f 
            GPIO.output(self.gPin,0) #g
        else:
            GPIO.output(self.aPin,1) #a
            GPIO.output(self.bPin,1) #b
            GPIO.output(self.cPin,1) #c
            GPIO.output(self.dPin,1) #d
            GPIO.output(self.ePin,1) #e
            GPIO.output(self.fPin,1) #f 
            GPIO.output(self.gPin,0) #g

def signalProcess(channel):
    # button has been pushed
    print("Button was pushed! You must wait 20 seconds to push again.")
    # traffic light 2 turns to blue blink 3 times then turns red
    LED2.turnBlue()
    sleep(1)
    LED2.turnOff()  # blink 1
    sleep(1)
    LED2.turnBlue()
    sleep(1)
    LED2.turnOff()  # blink 2
    sleep(1)
    LED2.turnBlue()
    sleep(1)
    LED2.turnOff()  # blink 3
    sleep(1)
    LED2.turnRed()
    # traffic light 1 becomes green and the countdown panel begins to count down from 9 to 0, in seconds
    LED1.turnGreen()
    SEGMENT.display(9)
    sleep(1)
    SEGMENT.display(8)
    sleep(1)
    SEGMENT.display(7)
    sleep(1)
    SEGMENT.display(6)
    sleep(1)
    SEGMENT.display(5)
    sleep(1)
    SEGMENT.display(4)
    # when countdown reaches 4, the traffic light 1 flashes with blue light until time 0.
    LED1.turnBlue()
    sleep(1)
    SEGMENT.display(3)
    LED1.turnOff()
    sleep(1)
    SEGMENT.display(2)
    LED1.turnBlue()
    sleep(1)
    SEGMENT.display(1)
    LED1.turnOff()
    sleep(1)         
    SEGMENT.display(0)
    # when countdown reaches 0, the traffic light 1 becomes red, traffic light 2 becomes green.
    LED1.turnRed()
    LED2.turnGreen()
    # when the button is pressed once there will be a 20 seconds cooldown to be able to make another valid press.
    sleep(5)

# Signal Handler function - exits during keyboard interrupt
def signal_handler(sig, frame):
	GPIO.cleanup()
	sys.exit(0)

# Initializing variables
LED1 = led1(GPIO.setup(led1RedPin,GPIO.OUT), led1RedPin, GPIO.setup(led1GreenPin,GPIO.OUT), led1GreenPin, 
            GPIO.setup(led1BluePin,GPIO.OUT), led1BluePin)
LED2 = led2(GPIO.setup(led2RedPin,GPIO.OUT), led2RedPin, GPIO.setup(led2GreenPin,GPIO.OUT), led2GreenPin, 
            GPIO.setup(led2BluePin,GPIO.OUT), led2BluePin)
GPIO.setup(buttonPin, GPIO.IN, GPIO.PUD_DOWN)
SEGMENT = segment(GPIO.setup(segmentAPin,GPIO.OUT), segmentAPin, GPIO.setup(segmentBPin,GPIO.OUT), segmentBPin, 
            GPIO.setup(SegmentCPin,GPIO.OUT), SegmentCPin, GPIO.setup(segmentDPin,GPIO.OUT), segmentDPin, 
            GPIO.setup(segmentEPin,GPIO.OUT), segmentEPin, GPIO.setup(segmentFPin,GPIO.OUT), segmentFPin,
            GPIO.setup(segmentGPin,GPIO.OUT), segmentGPin)
print('Traffic lights have begun!')

# Polling Method
"""
try:
    while 1:
        LED2.turnGreen()
        LED1.turnRed()
        if (GPIO.input(buttonPin) == GPIO.HIGH):
            signalProcess(0)
finally:
    GPIO.cleanup()
"""
# Interrupt Method
LED2.turnGreen()
LED1.turnRed()
GPIO.add_event_detect(buttonPin, GPIO.RISING, signalProcess, 100)
signal.signal(signal.SIGINT, signal_handler)
signal.pause()