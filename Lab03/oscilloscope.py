'''
Names: Cristian Avalos, Hariharan Sivakumar
Class: CSCE-462
Date Began: 2/23/2021
lab03 - Interfacing Analog To Digitalconverter (ADC) With A Microcontroller
'''
# necessary imports
import os
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time
from math import pi, sin

# setting up board and ADC chip
# create spi bus
spi = busio.SPI(clock = board.SCK, MISO = board.MISO, MOSI = board.MOSI)

# create the chip select
cs = digitalio.DigitalInOut(board.D22)

# create MCP object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0 of ADC
inputChan = AnalogIn(mcp, MCP.P0)

def cleanUpData(rawData):
  # This function will sort the raw data and non repeating values onto a new list
  # i.e. multiple 0 values
  cleanData = []
  rawData.sort()
  for i in rawData:
    if i not in cleanData: 
      cleanData.append(i)
  return cleanData

def waveFrequency():
  # We will gather a number points at or close to 0, time them, and find the difference for period
  # We will then average the periods to find our estimated frequency
  averagePeriod = 0
  for i in range(0, 100):
    while(inputChan.voltage > 0):
      pass
    while(inputChan.voltage < 0.01):
      pass
    startTime = time.time()
    while(inputChan.voltage > 0):
      pass
    while(inputChan.voltage < 0.01):
      pass
    endTime = time.time()
    averagePeriod += (endTime - startTime)
  averagePeriod /= 100
  return (1 / averagePeriod)

def recognizeWave():
  # We will gather a number of random points from the wave to determine the shape and add them to lists
  rawDataPoints = []
  cleanDataPoints = []
  # Gathering raw data
  for i in range(0, 100):
    rawDataPoints.append(inputChan.voltage)
# Clean up the raw data
  cleanDataPoints = cleanUpData(rawDataPoints)

  # This section will determine if the shape is a square wave
  checkSquare = True
  # This for loop will compare the data points with the max voltage with a small error
  # Since square waves have a constant voltage of max and 0, we can skip the 0v
  # And compare all of the other voltages with the max
  for i in range(len(cleanDataPoints)):
    if (cleanDataPoints[i] == 0):
      continue
    elif (cleanDataPoints[i] > (max(cleanDataPoints) - 0.1)):
        continue
    else:
      checkSquare = False
      break
  if (checkSquare):
    return "square wave"
  
  # This section will determine if the shape is a triangle wave
  checkTriangle = True
  initialSlope = (cleanDataPoints[1] - cleanDataPoints[0]) / (len(cleanDataPoints) - 1)
  
  # This for loop would compare the slope of the first two points with the remainder of the 
  # Points since triangle waves have a constant stope
  for i in range(len(cleanDataPoints) - 1):
    currentSlope = (cleanDataPoints[i + 1] - cleanDataPoints[i]) / (len(cleanDataPoints) - 1)
    #print(initialSlope,currentSlope)
    if (abs(initialSlope - currentSlope) < (0.003)):
      continue
    else:
      checkTriangle = False
      break
  if (checkTriangle and initialSlope != 0):
    return "triangle wave"
  # This section will determine if the shape is a sine wave 
  return "sine wave"
# main function
''''
currentWave = recognizeWave()
print("The wave is most likely a ", recognizeWave(), " with a frequency of ", waveFrequency(), "Hz.\n")
while (True):
  if (currentWave != recognizeWave()):
    print("The wave is most likely a ", recognizeWave(), " with a frequency of ", waveFrequency(), "Hz.\n")
    currentWave = recognizeWave()
'''
while(True):
    print("The wave is most likely a ",recognizeWave())
  print("Frequency: ", waveFrequency())
  print("\n")
