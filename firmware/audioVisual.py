import sys
import datetime
import time
import serial
import datetime
import os
import csv
import time
import matplotlib.patches as mpatches
# from getmac import get_mac_address
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

from mintsXU4 import mintsVisual as mV
from mintsXU4 import mintsDefinitions as mD
from matplotlib import style
import numpy as np

dataFolder = mD.dataFolder
# macAddress = mD.macAddress

plt.style.use('ggplot')

macAddress = "0242a1ee49fb"

RATE = 16000
CHUNK = 1024 # 1024bytes of data red from a buffer
INTERVAL = 1/RATE




def main():

    keepGoing = True
    frequenciesIn = np.linspace(0.0, 1.0/(2.0*INTERVAL), CHUNK//2)
    SensorName ="MI305"
    lineIn = []
    while keepGoing:
        try:
            amplitudesIn = []

            MI305 ,valid    = mV.readJSONLatestAll(SensorName)
            if(valid):
                for (keyIn,valueIn) in MI305.items():
                    if keyIn == "dateTime":
                        dateTime = str(valueIn)
                        print("DateTime: " + str(dateTime))
                    else:
                        amplitudesIn.append(valueIn)

            print("----------------------")
            maxInd = np.argmax(amplitudesIn)
            dateTimePatch = mpatches.Patch(color='black', label="Last Updated: " + str(dateTime))
            bluePatch     = mpatches.Patch(color='blue',  label="Max Frequency: "+ str(frequenciesIn[maxInd]))
            legendsIn = [dateTimePatch,bluePatch]
            lineIn = mV.mintsLivePlotter(frequenciesIn,amplitudesIn,\
                                         "Frequencies(Hz)",\
                                         "Amplitude","Amplitude Vs Frequency - "+ SensorName ,\
                                         lineIn,\
                                         legendsIn,
                                         0.1)
            print(len(amplitudesIn))
            print(max(amplitudesIn))
            print("----------------------")

            amplitudesIn = []
            time.sleep(0.1)

        except KeyboardInterrupt:
            keepGoing=False

        except:
            pass

        # amplitudesIn = []

def mintsLiveBarPlotter(xData,yData,xLabel,yLabel,title,lineIn,legendsIn,pauseIn):
    if lineIn==[]:
        my_dpi=96
        plt.ion()
        fig = plt.figure(figsize=(800/my_dpi, 450/my_dpi), dpi=my_dpi)
        ax  = fig.add_subplot(111)
        lineIn, = ax.plot(xData,yData,'-b',alpha=0.8)
        plt.ylabel(yLabel)
        plt.xlabel(xLabel)
        plt.title(title)
        plt.legend(handles=legendsIn)
        # plt.legend(handles=[blue_patch])
        plt.show()


    lineIn.set_ydata(yData)

    if np.min(yData)<=lineIn.axes.get_ylim()[0] or np.max(yData)>=lineIn.axes.get_ylim()[1]:
        plt.ylim([np.min(yData)-np.std(yData),np.max(yData)+np.std(yData)])
    plt.pause(pauseIn)


    return lineIn
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

# use ggplot style for more sophisticated visuals


# def mintsLivePlotter(xData,yData,xLabel,yLabel,title,lineIn,legendsIn,pauseIn):
#     if lineIn==[]:
#         my_dpi=96
#         plt.ion()
#         fig = plt.figure(figsize=(800/my_dpi, 450/my_dpi), dpi=my_dpi)
#         ax  = fig.add_subplot(111)
#         lineIn, = ax.plot(xData,yData,'-b',alpha=0.8)
#         plt.ylabel(yLabel)
#         plt.xlabel(xLabel)
#         plt.title(title)
#         plt.legend(handles=legendsIn)
#         # plt.legend(handles=[blue_patch])
#         plt.show()
#
#
#     lineIn.set_ydata(yData)
#
#     if np.min(yData)<=lineIn.axes.get_ylim()[0] or np.max(yData)>=lineIn.axes.get_ylim()[1]:
#         plt.ylim([np.min(yData)-np.std(yData),np.max(yData)+np.std(yData)])
#     plt.pause(pauseIn)
#
#
#     return lineIn



if __name__ == '__main__':
  main()
