'''
Names:
	Hariharan Sivakumar
	Cristian Avalos
Lab 4: 
	Inertial Measurement Units
Date Began:
	03/11/2021
'''
import board
import busio
import adafruit_mpu6050
import matplotlib.pyplot as plt
from time import sleep, perf_counter
import time
import math
from scipy.stats import linregress
i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

# Data for Chart
gyro_data = []
timeLog = []
# Data for step count
gyroX = []
gyroY = []
gyroZ = []
timeTracker = []
stepCounterX = 0
stepCounterY = 0
stepCounterZ = 0
time_start = perf_counter()
# Threshholds to determine step taken
avgSlopeThresh = 0.01
xThreshhold = 40
yThreshhold = 20
zThreshhold = 20

def clearLists(list1, list2, list3):
  list1.clear()
  list2.clear()
  list3.clear()
  
# main
print('Starting step reading...')
print('Use CTRL-C to top to display data')

sleep(1)
try:
    while True:
      	# Gathering data for the chart
        gyro_data.append(mpu.gyro)
        time_step = perf_counter()
        timeLog.append(time_step - time_start)
        # Gathering data for step count
        gyroX.append(mpu.gyro[0])
        gyroY.append(mpu.gyro[1])
        gyroZ.append(mpu.gyro[2])
        timeTracker.append(time.time())
        sleep(0.2) 
        gyroX.append(mpu.gyro[0])
        gyroY.append(mpu.gyro[1])
        gyroZ.append(mpu.gyro[2])
        timeTracker.append(time.time())
        # Finding slopes of each line
        # Will take a bit longer because of the lineregress function	
        slopeX, intercept, r_value, p_value, std_err = linregress(gyroX, timeTracker)
        slopeY, intercept, r_value, p_value, std_err = linregress(gyroY, timeTracker)
        slopeZ, intercept, r_value, p_value, std_err = linregress(gyroZ, timeTracker)
        averageslope = (slopeX + slopeY + slopeZ) / 3
        if (abs(averageslope) <= avgSlopeThresh) and (abs(gyroX[-1]) > xThreshhold) and (abs(gyroY[-1]) > yThreshhold) and (abs(gyroZ[-1]) > zThreshhold): 
            stepCounterX += 1
            stepCounterY += 1
            stepCounterZ += 1
            print("Number of steps taken: ", math.floor((stepCounterX + stepCounterY + stepCounterZ) / 3))
        
    sleep(0.00001)
    clearLists(gyroX, gyroY, gyroZ)
    timeTracker.clear()
except KeyboardInterrupt:
        clearLists(gyroX, gyroY, gyroZ)
        for i in range(len(gyro_data)):
            gyroX.append(gyro_data[i][0])
            gyroY.append(gyro_data[i][1])
            gyroZ.append(gyro_data[i][2])

        plt.plot(timeLog, gyroX, label = "x")
        plt.plot(timeLog, gyroY, label = "y")
        plt.plot(timeLog, gyroZ, label = "z")
        plt.xlabel("Time (s)")
        plt.ylabel("Gyro (degrees/s)")
        plt.legend()
        plt.show()

