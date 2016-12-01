import time
from datetime import datetime
from pymongo import MongoClient
import geopy
from geopy.distance import VincentyDistance

client = MongoClient()
db = client.testDB

recordsFutian = []
futianCenter = geopy.Point(22.543, 114.055)
northLat = VincentyDistance(kilometers=2).destination(futianCenter, 0).latitude
southLat = VincentyDistance(kilometers=2).destination(futianCenter, 180).latitude
eastLon = VincentyDistance(kilometers=2).destination(futianCenter, 90).longitude
westLon = VincentyDistance(kilometers=2).destination(futianCenter, 270).longitude
print(northLat, southLat, eastLon, westLon)
with open('./confidentialData/GPS_2016_01_02', 'rb') as file:
    while True:
        entry = file.readline().decode('utf-8')
        if entry == "":
            break
        else:
            infoArray = entry.split(',')

            # 01  . license plate
            # TODO: write regular expressions to check the data validity
            try:
                licensePlate = infoArray[0]
            except:
                print(entry)

            # 1. time
            try:
                timestamp = datetime.strptime(infoArray[3], "%Y-%m-%d %X")
                timeInNumber = time.mktime(timestamp.timetuple())
            except:
                print(entry)

            # 2.longitude
            try:
                if (float(infoArray[1]) > westLon and float(infoArray[1]) <eastLon):
                    longitude = float(infoArray[1])
                elif (float(infoArray[1]) * 10 > westLon and float(infoArray[1])*10 < eastLon):
                    longitude = float(infoArray[1]) * 10
                else:
                    continue
            except:
                print(entry)

            # 3. latitude
            try:
                if (float(infoArray[2]) > southLat and float(infoArray[2]) < northLat):
                    latitude = float(infoArray[2])
                elif (float(infoArray[2]) * 10 > southLat and float(infoArray[2]) * 10 < northLat):
                    latitude = float(infoArray[2]) * 10
                else:
                    continue
            except:
                print(entry)


            oneRecord = {"licensePlate": licensePlate, "latitude": latitude,
                         "longitude": longitude, "timeRecorded": timeInNumber}
            recordsFutian.append(oneRecord)
    print(len(recordsFutian))
    result = db.futian.insert(recordsFutian)
