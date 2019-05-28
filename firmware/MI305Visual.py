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

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


dataFolder = mD.dataFolder
macAddress = mD.macAddress

plt.style.use('ggplot')


RATE = 16000
CHUNK = 1024 # 1024bytes of data red from a buffer
INTERVAL = 1/RATE

my_dpi=96
fig = plt.figure(figsize=(800/my_dpi, 450/my_dpi), dpi=my_dpi)
ax1 = fig.add_subplot(1,1,1)

def main():
    ani = animation.FuncAnimation(fig, animateAudio, interval=500)
    plt.show()


def animateAudio(i):
    try:
        SensorName ="MI305"
        amplitudesIn = []
        frequenciesIn = np.linspace(0.0, 1.0/(2.0*INTERVAL), CHUNK//2)
        MI305 ,valid    = mV.readJSONLatestAll(SensorName)
        if(valid):
            for (keyIn,valueIn) in MI305.items():
                if keyIn == "dateTime":
                    dateTime = str(valueIn)

                else:
                    amplitudesIn.append(valueIn)

            maxInd = np.argmax(amplitudesIn)
            maxFrequency = frequenciesIn[maxInd]
            dateTimePatch = mpatches.Patch(color='black', label="Last Updated: " + str(dateTime))
            bluePatch     = mpatches.Patch(color='blue',  label="Max Frequency: "+ str(maxFrequency))
            print("----------------------")
            print("DateTime         : " + str(dateTime))
            print("Maximum Frequency: " + str(maxFrequency))
            print("----------------------")
            legendsIn = [dateTimePatch,bluePatch]
            ax1.clear()
            ax1.plot(frequenciesIn,amplitudesIn)
            ax1.set_ylabel("Amplitude")
            ax1.set_xlabel("Frequency(Hz)")
            ax1.set_title("Amplitude vs Frequency - "+ SensorName)
            ax1.legend(handles=legendsIn)
    except KeyboardInterrupt:
        print("-- MINTS QUITING --")

    except:
        pass




if __name__ == '__main__':
  main()
