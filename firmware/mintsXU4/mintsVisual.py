

# import serial
# ser = serial.Serial('/dev/ttyACM3')
import serial
import datetime
import os
import csv
import time
import json
import matplotlib.patches as mpatches
# from getmac import get_mac_address
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from mintsXU4 import mintsDefinitions as mD

dataFolder = mD.dataFolder
macAddress = mD.macAddress


def writeJSONLatest(sensorDictionary,sensorName):
    # print(writePath)
    directoryIn  = dataFolder+"/"+macAddress+"/"+sensorName+".json"
    # print(directoryIn)
    try:
    	with open(directoryIn,'w') as fp:
    	    json.dump(sensorDictionary, fp)
    except:
        print("Data Conflict!")

def readJSONLatestAll(sensorName):
    try:
        directoryIn  = dataFolder+"/"+macAddress+"/"+sensorName+".json"
        with open(directoryIn, 'r') as myfile:
            # dataRead=myfile.read()
            dataRead=json.load(myfile)

        time.sleep(0.01)
        return dataRead, True
    except:
        print("Data Conflict!")
        return "NaN", False


def mintsLivePlotter(xData,yData,xLabel,yLabel,title,lineIn,legendsIn,pauseIn):
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
        plt.legend(handles=legendsIn)
    plt.pause(pauseIn)


    return lineIn
