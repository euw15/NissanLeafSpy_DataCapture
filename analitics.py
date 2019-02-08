import csv
from os import listdir
from os.path import isfile, join

c_TimeStampIndex    = 0
c_LatPointsIndex    = 1
c_LongPointsIndex   = 2
c_ElevPointsIndex   = 3
c_SpeedPointsIndex  = 4
c_SOCPointsIndex    = 6
c_TempPointsIndex   = 130
c_SOHPointsIndex    = 131
c_RegenPointsIndex  = 132
c_MotorPowerPoints  = 135
c_ACPowerIndex      = 139
c_PlugPointsIndex   = 141
c_BMSIndex   = 149

class RideData:
    timeStamp = []
    gpsPoints = []
    elevationPoints = []
    SOCPoints = []
    speedPoints = []
    regenWhPoints = []
    avgElevation = 0
    avgSpeed = 0
    difSoc = 0
  
    def __init__(self, timeStamp, gpsPoints, elevationPoints, SOCPoints, speedPoints, regenWhPoints, avgElevation, avgSpeed, difSoc):
        self.timeStamp          = timeStamp
        self.gpsPoints          = gpsPoints
        self.elevationPoints    = elevationPoints
        self.SOCPoints          = SOCPoints
        self.speedPoints        = speedPoints
        self.regenWhPoints      = regenWhPoints
        self.avgElevation       = avgElevation
        self.avgSpeed           = avgSpeed
        self.difSoc             = difSoc

    def PrintAllData(self):
        print("AVG Elevation: " + str(self.avgElevation) )
        print("AVG Speed: " + str(self.avgSpeed))
        print("DIF SOC: " + str(self.difSoc))
        print("---Time---")
        print(self.timeStamp);
        print("---GPS---")
        print(self.gpsPoints);
        print("---Elevation---")
        print(self.elevationPoints);
        print("---SOC---")
        print(self.SOCPoints);
        print("---Speed---")
        print(self.speedPoints);
        print("---Regen---")
        print(self.regenWhPoints);

allRidesData = []

mypath = 'C:\\Users\\umanaedw\\Downloads\\Log Files\\'

allFiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

with open('C:\\Users\\umanaedw\\Downloads\\Log Files\\Log_DC421447_170601_FC8E8.csv', 'r') as cvs_file:
    csv_reader = csv.reader(cvs_file)

    timeStamp = []
    gpsPoints = []
    elevationPoints = []
    SOCPoints = []
    speedPoints = []
    regenWhPoints = []
    
    for line in csv_reader:
        timeStamp.append(line[c_TimeStampIndex])
        gpsPoints.append([line[c_LatPointsIndex],line[c_LongPointsIndex]])
        elevationPoints.append(line[c_ElevPointsIndex])
        SOCPoints.append(line[c_SOCPointsIndex])
        speedPoints.append(line[c_SpeedPointsIndex])
        regenWhPoints.append(line[c_RegenPointsIndex])

    timeStamp.pop(0)
    gpsPoints.pop(0)
    elevationPoints.pop(0)
    SOCPoints.pop(0)
    speedPoints.pop(0)
    regenWhPoints.pop(0)

    rideData = RideData(timeStamp,gpsPoints,elevationPoints,SOCPoints,speedPoints,regenWhPoints, 1231, 23, 26.875)
    allRidesData.append(rideData)

    for ride in allRidesData:
        ride.PrintAllData()
 
