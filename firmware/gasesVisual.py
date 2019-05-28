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
import numpy.ma as ma
dataFolder = mD.dataFolder
# macAddress = mD.macAddress

plt.style.use('ggplot')

macAddress = "0242a1ee49fb"

RATE = 16000
CHUNK = 1024 # 1024bytes of data red from a buffer
INTERVAL = 1/RATE



def main():

    keepGoing = True
    boundriesIn =  [0.35,0.46,0.66,1.0,1.3,1.7,2.3,3.0,4.0,5.2,\
                    6.5,8.0,10.0,12.0,14.0,16.0,18.0,20.0,22.0,25.0,\
                    28.0,31.0,34.0,37.0,40]

    diametorsInPre = boundriesIn[:-1] + np.diff(boundriesIn)/2
    diametorsInPre2= []
    for x in diametorsInPre:
        diametorsInPre2.append(round(x,2))
    diametorsIn = tuple(diametorsInPre2)


    print(diametorsIn)
    SensorName ="OPCN3"
    lineIn = []
    binCounts = []
    amplitudesIn = []
    rectsNew  = True
    while keepGoing:
        # try:
        OPCN3 ,valid    = mV.readJSONLatestAll(SensorName)
        if(valid):
            dateTime  = OPCN3['dateTime']
            binCounts = [ float(OPCN3['binCount0']), \
                              float(OPCN3['binCount1']), \
                              float(OPCN3['binCount2']), \
                              float(OPCN3['binCount3']), \
                              float(OPCN3['binCount4']), \
                              float(OPCN3['binCount5']), \
                              float(OPCN3['binCount6']), \
                              float(OPCN3['binCount7']), \
                              float(OPCN3['binCount8']), \
                              float(OPCN3['binCount9']), \
                              float(OPCN3['binCount10']), \
                              float(OPCN3['binCount11']), \
                              float(OPCN3['binCount12']), \
                              float(OPCN3['binCount13']), \
                              float(OPCN3['binCount14']), \
                              float(OPCN3['binCount15']), \
                              float(OPCN3['binCount16']), \
                              float(OPCN3['binCount17']), \
                              float(OPCN3['binCount18']), \
                              float(OPCN3['binCount19']), \
                              float(OPCN3['binCount20']), \
                              float(OPCN3['binCount21']), \
                              float(OPCN3['binCount22']), \
                              float(OPCN3['binCount23']), \
                              ]
                # for (keyIn,valueIn) in OPCN3.items():
                #     if keyIn.startswith("binCount"):
                #         amplitudesIn.append(valueIn)
                #
        pm1   = str(OPCN3['pm1']).rjust(7," ")
        pm2_5 = str(OPCN3['pm2_5']).rjust(7," ")
        pm10  = str(OPCN3['pm10']).rjust(7," ")


        print("----------------------")
                # maxInd = np.argmax(amplitudesIn)
        dateTimePatch = mpatches.Patch(color='black', label="Last Updated: " + str(dateTime))
        bluePatch     = mpatches.Patch(color='blue',  label="PM2.5: "+ str(pm2_5))
        legendsIn     = [dateTimePatch,bluePatch]
        print(binCounts)


def animate()
    xData  = np.linspace(1,24,24)
    rects = plt.bar(xData, binCounts, align='center', alpha=0.5)
    plt.xticks(xData, diametorsIn, rotation='vertical')
    plt.ylabel('log(Particle Counts)')
    plt.xlabel('Particle Diametors')
    plt.title('Particle Distribution')
    plt.legend(handles=legendsIn)
    plt.show()
    plt.pause(2)

        # else:
        #     dateTimePatch = mpatches.Patch(color='black', label="Last Updated: " + str(dateTime))
        #     bluePatch     = mpatches.Patch(color='blue',  label="PM2.5: "+ str(pm2_5))
        #     legendsIn = [dateTimePatch,bluePatch]
        #     plt.legend(handles=legendsIn)
        #     for rect, h in zip(rects, binCounts):
        #         rect.set_height(h)
        #     # lineIn = mintsLiveBarPlotter(diametorsIn,\
        #     #                                  binCounts,\
        #     #                                  "Bin Diametors(uM)",\
        #     #                                  "Particle Counts",\
        #     #                                  "Particle Counts Vs Bin Diametors - "+ SensorName ,\
        #     #                                  lineIn,\
        #     #                                  legendsIn,\
        #     #                                  10)
        # time.sleep(2)
        #
        # # except KeyboardInterrupt:
        # #     keepGoing=False
        # #
        # # except:
        # #     pass
        #
        # # amplitudesIn = []


def mintsLiveBarPlotter(xLabels,yData,xLabel,yLabel,title,lineIn,legendsIn,pauseIn):
    my_dpi=96
    plt.ion()
    fig = plt.figure(figsize=(800/my_dpi, 450/my_dpi), dpi=my_dpi)
    ax  = fig.add_subplot(111)
    xData  = np.linspace(1,24,24)
    ax.bar(xData,yData, align='center', alpha=0.5)
    plt.xticks(xData,xLabels)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.title(title)
    plt.legend(handles=legendsIn)
    # plt.legend(handles=[blue_patch])
    plt.show()

    #
    # lineIn.set_ydata(yData)
    #
    # if np.min(yData)<=lineIn.axes.get_ylim()[0] or np.max(yData)>=lineIn.axes.get_ylim()[1]:
    #     plt.ylim([np.min(yData)-np.std(yData),np.max(yData)+np.std(yData)])
    # plt.pause(pauseIn)


    return lineIn




if __name__ == '__main__':
  main()
