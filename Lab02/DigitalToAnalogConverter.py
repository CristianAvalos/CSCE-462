'''
Names: Cristian Avalos, Hariharan Sivakumar
Class: CSCE-462
Date Began: 2/5/2021
lab02 - Use of Digital to Analog Converter along with a Microcontroller
'''
import time
import Adafruit_MCP4725
import Adafruit_GPIO
import RPi.GPIO as GPIO
from math import pi, sin, asin

dac = Adafruit_MCP4725.MCP4725()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

buttonPin = 17

def waveFunc(waveform, frequency, maxOutputVoltage):
    if (waveform == "square"):
        period = 1.0 / float(frequency)
        
        peak = 1.0
        while True:
            output = peak * float(maxOutputVoltage)
            dac.set_voltage(int(output))
            peak = -1.0 * peak
            if (GPIO.input(buttonPin) == GPIO.HIGH):
                return
    elif (waveform == "triangle"):
        amplitude = float(maxOutputVoltage)
        period = 1.0 / float(frequency)
        x = 0.00 
        while True:
            output = ((2 * amplitude) / pi) * asin(sin(((2 * pi) / period) * x))
            dac.set_voltage(int(abs(output)))
            x += 0.0005
            if (GPIO.input(buttonPin) == GPIO.HIGH):
                return
    elif (waveform == "sin"):    
        t = 0.0
        tStep = 0.01
        while True:
            output = float(maxOutputVoltage)*(1.0+0.5*sin(2*pi*frequency*t))
            dac.set_voltage(int(output))
            t += tStep
            time.sleep(0.0005)
            if (GPIO.input(buttonPin) == GPIO.HIGH):
                return
    
    else:
        print("Invalid option, try again!")
        return
# button pin setup
GPIO.setup(buttonPin, GPIO.IN, GPIO.PUD_DOWN)    
while (1):
  if (GPIO.input(buttonPin) == GPIO.HIGH):
    waveform = raw_input("What shape of waveform would you like? ")
    waveform = waveform.lower()
    if (waveform != "square" and waveform != "triangle" and waveform != "sin"):
        print("Invalid option! Only square, triangle, and sin")
        continue
    frequency = raw_input("What would you like the frequency set to? (Max 20Hz) ")
    if (float(frequency) < 0 or float(frequency) > 20):
        print("Invalid range! Only ranges between 0 and 20!")
        continue
    maxOutputVoltage = raw_input("What is the maximum output voltage? ")
    if (float(maxOutputVoltage) < 0 or float(maxOutputVoltage) > 4095):
        print("Invalid range! Only ranges between 0 and 4095")
        continue
    waveFunc(waveform, frequency, maxOutputVoltage)
