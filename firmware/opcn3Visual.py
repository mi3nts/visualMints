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
    frequenciesIn = np.linspace(1,24,24)
    SensorName ="OPCN3"

    # style.use('fivethirtyeight')
    # fig = plt.figure()
    # ax1 = fig.add_subplot(1,1,1)
    lineIn = []
    while keepGoing:
        try:
            amplitudesIn = []

            OPCN3 ,valid    = mV.readJSONLatestAll(SensorName)
            if(valid):
                for (keyIn,valueIn) in OPCN3.items():
                    if keyIn == "dateTime":
                        dateTime = str(valueIn)
                        print("DateTime: " + str(dateTime))
                    if keyIn.startswith("binCount"):
                        amplitudesIn.append(float(valueIn))

            print("----------------------")
            maxInd = np.argmax(amplitudesIn)
            # dateTimePatch = mpatches.Patch(color='black', label="Last Updated: " + str(datetime.datetime.now()))
            bluePatch     = mpatches.Patch(color='blue',  label="Max Frequency: "+ str(frequenciesIn[maxInd]))
            legendsIn = [bluePatch]
            lineIn = mV.mintsLivePlotter(frequenciesIn,amplitudesIn,\
                                         "Frequencies(Hz)",\
                                         "Amplitude","Amplitude Vs Frequency - "+ SensorName ,\
                                         lineIn,\
                                         legendsIn,
                                         5)

            print(len(amplitudesIn))
            print(amplitudesIn)
            print(frequenciesIn)

            print("----------------------")

            # amplitudesIn = []
            time.sleep(5)

        except KeyboardInterrupt:
            keepGoing=False

        except:
            pass

if __name__ == '__main__':
  main()
