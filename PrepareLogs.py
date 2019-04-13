import csv
from datetime import datetime
from os import listdir
from os.path import isfile, join

#Time format
timeFormat = '%m/%d/%Y %H:%M:%S'
timeFormat2 = '%Y/%m/%d %H:%M:%S'

#Ruta donde estan los archivos
s_myPath = '.\\Logs\\'

#idNumber
idRide = 1

#Indice del tiermpo del cvs
c_TimeStampIndex    = 0

#Lista con el nombre de todos los archivos que estan en la carpeta myPath
l_allFilesList = [f for f in listdir(s_myPath) if isfile(join(s_myPath, f))]
  
def DivideRides(file):
    global idRide

    fileAsTxt=open(file)
    txtLines=fileAsTxt.readlines()
    currentLine = 0;
    
    #abro el archivo cvs original
    with open(file, 'r') as cvs_file:
        csv_reader = csv.reader(cvs_file)
    
        #creo el primer archivo secundario
        f = open(s_myPath + "Ride_"+str(idRide)+".csv","w+")

        isfirstLine = True
        isSecondLine = True
        #linea por linea 
        for line in csv_reader:
            try :
                timeFormat = '%m/%d/%Y %H:%M:%S'
                datetime.strptime(line[c_TimeStampIndex], timeFormat)
            except ValueError :
                timeFormat = '%Y/%m/%d %H:%M:%S'
            if(isfirstLine):
                isfirstLine = False
            elif(isSecondLine):
                isSecondLine = False
                oldTime = nowTime = datetime.strptime(line[c_TimeStampIndex], timeFormat)
                f.write(txtLines[currentLine])
                currentLine = 1
            else:
                f.write(txtLines[currentLine])
                nowTime = datetime.strptime(line[c_TimeStampIndex], timeFormat)
                dif = nowTime-oldTime
                oldTime = nowTime
                #si han pasado mas de 5 mims lo divide
                if(dif.seconds > 300):
                    f.close()
                    idRide+=1
                    f = open(s_myPath +"Ride_"+str(idRide)+".csv","w+") 
                currentLine += 1
        f.close()        
   
#Lista con todos los archivos
for rideFile in l_allFilesList:
    DivideRides(s_myPath+rideFile)
