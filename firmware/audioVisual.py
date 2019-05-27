import sys
import datetime
import time
import serial
import datetime
import os
import csv
import time
from getmac import get_mac_address
import matplotlib.pyplot as plt
from mintsXU4 import mintsVisual as mV
from mintsXU4 import mintsDefinitions as mD
from matplotlib import style
import numpy as np

dataFolder = mD.dataFolder
macAddress = mD.macAddress

RATE = 16000
CHUNK = 1024 # 1024bytes of data red from a buffer
INTERVAL = 1/RATE


frequenciesIn = np.linspace(0.0, 1.0/(2.0*INTERVAL), CHUNK//2)


def main():
    keepGoing = True
    fig, ax = plt.subplots()
    while keepGoing:
        try:
            amplitudesIn = []
            MI305 ,valid    = mV.readJSONLatestAll("MI305")
            if(valid):
                for (keyIn,valueIn) in MI305.items():

                    if keyIn == "dateTime":
                        dateTime = str(valueIn)
                        print("DateTime: " + str(dateTime))
                    else:
                        amplitudesIn.append(valueIn)

            print("----------------------")
            print(len(amplitudesIn))
            print(max(amplitudesIn))
            print("----------------------")
            ax.set_xlabel('Time (s)')
            ax.set_ylabel('Temperature (F)')
            ax.set_title("Your drink's current temperature")



            ax.plot(frequenciesIn,amplitudesIn)
            ax.grid()

            ax.pause(1)

            ax.clf()

            amplitudesIn = []
            time.sleep(0.15)

        except KeyboardInterrupt:
            keepGoing=False
            ax.close()
        except:
            pass

        # amplitudesIn = []


        # OPCN3,valid    = mL.readJSONLatestAll("OPCN3")
        # # if(valid):
        # #      pm1   = str(OPCN3['pm1']).rjust(7," ")
        # #      pm2_5 = str(OPCN3['pm2_5']).rjust(7," ")
        # #      pm10  = str(OPCN3['pm10']).rjust(7," ")
        # #      # getPMDecimals(pm10)
        # BME280,valid    = mL.readJSONLatestAll("BME280")
        # if(valid):
        #      # print(BME280)
        #      temperature = BME280['temperature']
        #      humidity    = BME280['humidity']
        #      pressure    = BME280['pressure']
        #
        # FLIR001,valid    = mL.readJSONLatestAll("FLIR001")
        # if(valid):
        #      # print(FLIR001)
        #      maxTemperature = str(FLIR001['maxTemperature'])
        #      minTemperature = str(FLIR001['minTemperature'])
        #
        #
        # printData(pm1,pm2_5,pm10,temperature,pressure,humidity,maxTemperature,minTemperature)

if __name__ == '__main__':
  main()
