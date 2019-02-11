mile = 1.60934

class RideData:
    timeStamp       = []
    gpsPoints       = []
    elevationPoints = []
    GIDPoints       = []
    SOCPoints       = []
    speedPoints     = []
    regenWhPoints   = []
    avgElevation    = 0
    avgDescent      = 0
    avgSpeed        = 0
    difSoc          = 0
    difGID          = 0
    soh             = 0
    distance        = 0
    duration        = 0
    filePath        = ''
    
    def __init__(self, timeStamp, gpsPoints, elevationPoints, SOCPoints, GIDPoints, speedPoints, regenWhPoints,
                 avgElevation, avgDescent, avgSpeed, difSoc, difGID, distance, duration, filePath, soh):
        self.timeStamp          = timeStamp
        self.gpsPoints          = gpsPoints
        self.elevationPoints    = elevationPoints
        self.GIDPoints          = GIDPoints
        self.SOCPoints          = SOCPoints
        self.speedPoints        = speedPoints
        self.regenWhPoints      = regenWhPoints
        self.avgElevation       = avgElevation
        self.avgDescent         = avgDescent
        self.avgSpeed           = avgSpeed
        self.difSoc             = difSoc
        self.difGID             = difGID
        self.distance           = distance
        self.duration           = duration
        self.filePath           = filePath
        self.soh                = soh
        
    def PrintAVGData(self):
        print("Archivo: " + self.filePath.split('\\')[-1])
        print("Elevación " + str(self.avgElevation) + "m" )
        print("Descenso: " + str(self.avgDescent) + "m")
        print("Velocidad Promedio: " + str(float("{0:.2f}".format(self.avgSpeed*mile)))+ "km/h")
        print("SOC Inicial: " + str(float(self.SOCPoints[0])/10000) + "%")
        print("SOC Final: " + str(float(self.SOCPoints[-1])/10000) + "%")
        print("DIF SOC: " + str(self.difSoc) + "%")
        print("Potencia Consumida: " + str(self.difGID*80) + " Wh")
        print("Distancía: " + str(self.distance) + "km")
        print("Duración: " + str(self.duration))
        print("SOH:  " + str(self.soh))
        
        
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
