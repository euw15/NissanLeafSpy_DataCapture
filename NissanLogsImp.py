import csv
from RideDataStruct import *
from UtilitiesAnalytics import *

#General Method that takes a file with full path and creates a RideData Object with the CSV information
def GetDataNissanSpyFile(file):
    with open(file, 'r') as cvs_file:
        csv_reader = csv.reader(cvs_file)

        timeStamp       = []
        gpsPoints       = []
        elevationPoints = []
        SOCPoints       = []
        speedPoints     = []
        regenWhPoints   = []
        GIDSPoints      = []
        SOH = 0
        
        for line in csv_reader:
            timeStamp.append(line[c_TimeStampIndex])
            gpsPoints.append([line[c_LatPointsIndex],line[c_LongPointsIndex]])
            elevationPoints.append(line[c_ElevPointsIndex])
            SOCPoints.append(line[c_SOCPointsIndex])
            speedPoints.append(line[c_SpeedPointsIndex])
            regenWhPoints.append(line[c_RegenPointsIndex])
            GIDSPoints.append(line[c_GIDPointsIndex])
            SOH =  line[c_SOHPointsIndex]

        #Elimina el primer elemento de la lista ya que no son datos, si no los tags
        timeStamp.pop(0)
        gpsPoints.pop(0)
        elevationPoints.pop(0)
        SOCPoints.pop(0)
        speedPoints.pop(0)
        regenWhPoints.pop(0)
        GIDSPoints.pop(0)

        for gpsPoint in gpsPoints:
            gpsPoint[0] = convertGPSToDecimal(gpsPoint[0])
            gpsPoint[1] = convertGPSToDecimal(gpsPoint[1])

        elevation   = CalculateElevation(elevationPoints)
        descent     = CalculateDescent(elevationPoints)
        distance    = CalculateRideDistance(gpsPoints)
        socDif      = CalculateSOCDif(SOCPoints)
        gidDif      = CalculateGIDSDif(GIDSPoints)
        avgSpeed    = sum(list(map(float, speedPoints))) / float(len(speedPoints))
        duration    = CalculateDuration(timeStamp,'%m/%d/%Y %H:%M:%S')

        
        rideData    = RideData(timeStamp,gpsPoints,elevationPoints,SOCPoints,GIDSPoints,speedPoints,regenWhPoints, elevation,
                               descent, avgSpeed, socDif, gidDif, distance, duration, file, SOH)
        return rideData
