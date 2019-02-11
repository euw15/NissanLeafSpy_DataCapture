mile = 1.60934

class RideData:
    timeStamp       = []
    gpsPoints       = []
    elevationPoints = []
    SOCPoints       = []
    speedPoints     = []
    regenWhPoints   = []
    avgElevation    = 0
    avgDescent      = 0
    avgSpeed        = 0
    difSoc          = 0
    distance        = 0

    def __init__(self, timeStamp, gpsPoints, elevationPoints, SOCPoints, speedPoints, regenWhPoints, avgElevation, avgDescent, avgSpeed, difSoc, distance):
        self.timeStamp          = timeStamp
        self.gpsPoints          = gpsPoints
        self.elevationPoints    = elevationPoints
        self.SOCPoints          = SOCPoints
        self.speedPoints        = speedPoints
        self.regenWhPoints      = regenWhPoints
        self.avgElevation       = avgElevation
        self.avgDescent         = avgDescent
        self.avgSpeed           = avgSpeed
        self.difSoc             = difSoc
        self.distance           = distance

    def PrintAVGData(self):
        print("Elevacion " + str(self.avgElevation) + "m" )
        print("Descenso: " + str(self.avgDescent) + "m")
        print("Velocidad Promedio: " + str(float("{0:.2f}".format(self.avgSpeed*mile)))+ "km/h")
        print("DIF SOC: " + str(self.difSoc) + "%")
        print("Distancia: " + str(self.distance) + "km")
        
    def PrintAllData(self):
        self.PrintAVGData()
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
