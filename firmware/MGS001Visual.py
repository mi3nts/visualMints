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

my_dpi=96
fig = plt.figure(figsize=(800/my_dpi, 450/my_dpi), dpi=my_dpi)
ax1 = fig.add_subplot(1,1,1)

def main():
    ani = animation.FuncAnimation(fig, animateMGS001, interval=500)
    plt.show()


def animateMGS001(i):
    try:
        SensorName ="MGS001"
        binCountsIn = []
        MGS001 ,valid    = mV.readJSONLatestAll(SensorName)
        if(valid):
            dateTime  = MGS001['dateTime']

            gases   = [ float(MGS001['nh3']),\
                        float(MGS001['co']),\
                        float(MGS001['no2']),\
                        float(MGS001['c3h8']),\
                        float(MGS001['c4h10']),\
                        float(MGS001['ch4']),\
                        float(MGS001['h2']),\
                        float(MGS001['c2h5oh'])\
                        ]

            dateTimePatch = mpatches.Patch(color='black', label="Last Updated: " + str(dateTime))
            legendsIn = [dateTimePatch]

            print("----------------------")
            print("DateTime: " + str(dateTime))
            print("----------------------")

            gasesIn = ("$NH_3$","$CO$","$NO_2$","$C_3H_8$","$C_4H_{10}$","$CH_4$","$H_2$","$C_2H_5OH$",)

            xData  = np.linspace(1,8,8)
            ax1.clear()
            ax1.bar(xData, gases, align='center', alpha=0.5,color="blue")
            ax1.set_xticks(xData)
            ax1.set_xticklabels(gasesIn)
            ax1.set_yscale('log')
            ax1.set_ylabel("Concentrations")
            ax1.set_xlabel("Gases")
            ax1.set_title(" Gas Concentrations - "+ SensorName)
            ax1.legend(handles=legendsIn)


    except KeyboardInterrupt:
        print("-- MINTS QUITING --")
        ax1.close()
    except:
        pass



if __name__ == '__main__':
  main()
