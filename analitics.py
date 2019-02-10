import csv
from os import listdir
from os.path import isfile, join
from math import sin, cos, sqrt, atan2, radians
import geopy.distance

#Indices de los datos que estan en los archivos CSV.
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

# approximate radius of earth in km
R = 6373.0

#Clase que tiene la informacion de un ride
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
    distance = 0

    def __init__(self, timeStamp, gpsPoints, elevationPoints, SOCPoints, speedPoints, regenWhPoints, avgElevation, avgSpeed, difSoc, distance):
        self.timeStamp          = timeStamp
        self.gpsPoints          = gpsPoints
        self.elevationPoints    = elevationPoints
        self.SOCPoints          = SOCPoints
        self.speedPoints        = speedPoints
        self.regenWhPoints      = regenWhPoints
        self.avgElevation       = avgElevation
        self.avgSpeed           = avgSpeed
        self.difSoc             = difSoc
        self.distance           = distance

    def PrintAVGData(self):
        print("AVG Elevation: " + str(self.avgElevation) )
        print("AVG Speed: " + str(self.avgSpeed))
        print("DIF SOC: " + str(self.difSoc))
        print("Distance: "+str(self.distance))
        
    def PrintAllData(self):
        print("AVG Elevation: " + str(self.avgElevation) )
        print("AVG Speed: " + str(self.avgSpeed))
        print("DIF SOC: " + str(self.difSoc))
        print("Distance: "+str(self.distance))
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

#General Method that takes a file with full path and creates a RideData Object with the CSV information
def GetDataFromFile(file):
    with open(file, 'r') as cvs_file:
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

        #Elimina el primer elemento de la lista ya que no son datos, si no los tags
        timeStamp.pop(0)
        gpsPoints.pop(0)
        elevationPoints.pop(0)
        SOCPoints.pop(0)
        speedPoints.pop(0)
        regenWhPoints.pop(0)

        for gpsPoint in gpsPoints:
            gpsPoint[0] = convertGPSToDecimal(gpsPoint[0])
            gpsPoint[1] = convertGPSToDecimal(gpsPoint[1])
            
        distance = CalculateRideDistance(gpsPoints);
        rideData = RideData(timeStamp,gpsPoints,elevationPoints,SOCPoints,speedPoints,regenWhPoints, 0, 0, 0,distance)
        return rideData

#9 54.34805
#-84 6.17203
def convertGPSToDecimal(coordinate):
    if(coordinate == ''):
        return -1;
    # split coordinate in 3 components and cast them to numbers
    degComponent = coordinate.split(' ')
    degrees = int(degComponent[0])
    multiplier = 1
    if(degrees < 0):
        degrees = abs(degrees)
        multiplier = -1;
    minAndSecComp = degComponent[1].split('.')
    components = coordinate
    minutes = int(minAndSecComp[0])
    seconds = int(minAndSecComp[1])

    # compute decimal coordinate with max 5 decimals
    calc = degrees + (minutes / 60) + (seconds / 3600)
    decimal_coordinate = float("{0:.5f}".format(multiplier*calc))

    return decimal_coordinate


def CalculateRideDistance(gpsPoints):
    distance = 0;
    cmpGPSPoint = gpsPoints[0]
    for gpsPoint in gpsPoints:
        print(distance)
        distance += DistanceBetweenTwoGPSPoints(cmpGPSPoint,gpsPoint)
        cmpGPSPoint = gpsPoint

    return distance

def DistanceBetweenTwoGPSPoints(beginPoint, endPoint):
    coords_1 = (beginPoint[0], beginPoint[1])
    coords_2 = (endPoint[0], endPoint[1])

    distance = geopy.distance.vincenty(coords_1, coords_2).km
    return distance

    
#Lista con todos los rides de todos los archivos 
allRidesData = []

#Ruta donde estan los archivos
mypath = 'C:\\Users\\umanaedw\\Downloads\\Test\\'

#Lista con el nombre de todos los archivos
allFilesList = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#Agrega todos los rides a una lista
for rideFile in allFilesList:
    allRidesData.append(GetDataFromFile(mypath+rideFile))

#Imprime todas las listas
for ride in allRidesData:
    ride.PrintAllData()
   

 
