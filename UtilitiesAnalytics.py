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

def CalculateElevation(elevationPoints):
    elevation = 0
    cmpPoint = elevationPoints[0]
    for elevationPoint in elevationPoints:
        if(cmpPoint <= elevationPoint):
            elevation +=  float(elevationPoint) - float(cmpPoint)
        cmpPoint = elevationPoint
    return elevation

def CalculateDescent(elevationPoints):
    elevation = 0
    cmpPoint = elevationPoints[0]
    for elevationPoint in elevationPoints:
        if(cmpPoint >= elevationPoint):
            elevation += float(cmpPoint) - float(elevationPoint)
        cmpPoint =  elevationPoint
    return elevation
