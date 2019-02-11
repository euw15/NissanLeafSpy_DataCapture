from os import listdir
from os.path import isfile, join
from NissanLogsImp import *
  
# Lista que almacena todos los rides de todos los archivos que
#que esten en la carpeta que apunte myPath 
l_allRidesData = []

#Ruta donde estan los archivos
s_myPath = 'C:\\Users\\umanaedw\\Downloads\\Test\\'

#Lista con el nombre de todos los archivos que estan en la carpeta myPath
l_allFilesList = [f for f in listdir(s_myPath) if isfile(join(s_myPath, f))]

#Agrega todos los rides a una lista
#GetDataFromFile es un metodo que lee espesificamente el log de NissanSpy
#Si se va a utilizar otro vendor se debe crear otro metodo
for rideFile in l_allFilesList:
    l_allRidesData.append(GetDataNissanSpyFile(s_myPath+rideFile))

#Impreme la informacion obtenida
for ride in l_allRidesData:
    ride.PrintAVGData()
   

 
