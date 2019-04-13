from math import sin, cos, sqrt, atan2, radians
from datetime import datetime
import geopy.distance

#Indices de los datos que estan en los archivos CSV.
c_TimeStampIndex    = 0
c_LatPointsIndex    = 1
c_LongPointsIndex   = 2
c_ElevPointsIndex   = 3
c_SpeedPointsIndex  = 4
c_GIDPointsIndex    = 5
c_SOCPointsIndex    = 6
c_TempPointsIndex   = 130
c_SOHPointsIndex    = 131
c_RegenPointsIndex  = 132
c_MotorPowerPoints  = 135
c_ACPowerIndex      = 139
c_PlugPointsIndex   = 141
c_BMSIndex          = 149


# approximate radius of earth in km
R = 6373.0

def convertGPSToDecimal(coordinate):
    if(coordinate == ''):
        return -1;
    # split coordinate in 2 components and cast them to numbers
    components  = coordinate.split(' ')
    degrees     = int(components[0])
    multiplier  = 1
    minutesComp = float(components[1])

    if(degrees < 0):
        degrees     = abs(degrees)
        multiplier  = -1;
        
    # compute decimal coordinate with max 7 decimals
    calc = degrees + (minutesComp / 60)
    decimal_coordinate = float("{0:.7f}".format(multiplier*calc))

    return decimal_coordinate


def CalculateRideDistance(gpsPoints):
    distance = 0
    cmpGPSPoint = gpsPoints[0]
    for gpsPoint in gpsPoints:
        distance += DistanceBetweenTwoGPSPoints(cmpGPSPoint,gpsPoint)
        cmpGPSPoint = gpsPoint

    return float("{0:.3f}".format(distance))


def DistanceBetweenTwoGPSPoints(beginPoint, endPoint):
    coords_1 = (beginPoint[0], beginPoint[1])
    coords_2 = (endPoint[0], endPoint[1])

    distance = geopy.distance.geodesic(coords_1, coords_2).km
    return distance


def CalculateSOCDif(SOCPoints):
    cmpSOCPoint = SOCPoints[0]
    socPoint    = SOCPoints[-1]
    dif = float(cmpSOCPoint) - float(socPoint)
    return dif/10000

def CalculateGIDSDif(SOCPoints):
    cmpSOCPoint = SOCPoints[0]
    socPoint    = SOCPoints[-1]
    dif = float(cmpSOCPoint) - float(socPoint)
    return dif

def CalculateElevation(gpsPoints, elevationPoints):
    elevDistance = 0
    i = 0
    elevation = 0
    while i < len(elevationPoints)-1:
        if(elevationPoints[i]  < elevationPoints[i+1]):
            elevation += int(elevationPoints[i+1]) - int(elevationPoints[i])
            elevDistance += DistanceBetweenTwoGPSPoints(gpsPoints[i],gpsPoints[i+1])
        i+= 1
    return (float("{0:.3f}".format(elevDistance)),elevation)

def CalculateDescent(gpsPoints, elevationPoints):
    descDistance = 0
    i = 0
    descent = 0
    while i < len(elevationPoints)-1:
        if(elevationPoints[i]  > elevationPoints[i+1]):
            descent += int(elevationPoints[i]) - int(elevationPoints[i+1]) 
            descDistance += DistanceBetweenTwoGPSPoints(gpsPoints[i],gpsPoints[i+1])
        i+= 1
    return (float("{0:.3f}".format(descDistance)),descent)
    
def CalculatePlane(gpsPoints, elevationPoints):
    planedistance = 0
    i = 0
    while i < len(elevationPoints)-1:
        if(elevationPoints[i]  == elevationPoints[i+1]):
            planedistance += DistanceBetweenTwoGPSPoints(gpsPoints[i],gpsPoints[i+1])
        i+= 1
    return float("{0:.3f}".format(planedistance))
        
def CalculateDuration(timeStampList,s_format):
    s_StarTime      = timeStampList[0]
    s_EndTime       = timeStampList[-1]
    try :
        timeFormat = '%m/%d/%Y %H:%M:%S'
        datetime.strptime(s_StarTime, timeFormat)
    except ValueError :
        timeFormat = '%Y/%m/%d %H:%M:%S'
    
    t_startTime     = datetime.strptime(s_StarTime, timeFormat)
    t_EndTime       = datetime.strptime(s_EndTime, timeFormat)
    return t_EndTime - t_startTime
    
