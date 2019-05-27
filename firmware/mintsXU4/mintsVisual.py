

# import serial
# ser = serial.Serial('/dev/ttyACM3')
import serial
import datetime
import os
import csv
import time
import json

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
