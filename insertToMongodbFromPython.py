import time
from datetime import datetime
from pymongo import MongoClient

client = MongoClient()
db = client.testDB

records = []
with open("GPS_2016_01_02", 'r') as file:
    while True:
        entry = file.readline()
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
                if (float(infoArray[1]) > 113.5 and float(infoArray[1]) < 115):
                    longitude = float(infoArray[1])
                elif (float(infoArray[1]) * 10 > 113.5 and float(infoArray[1])*10 < 115):
                    longitude = float(infoArray[1]) * 10
                else:
                    continue
            except:
                print(entry)

            # 3. latitude
            try:
                if (float(infoArray[2]) > 22 and float(infoArray[2]) < 23.15):
                    latitude = float(infoArray[2])
                elif (float(infoArray[2]) * 10 > 22 and float(infoArray[2]) * 10 < 23.15):
                    latitude = float(infoArray[2]) * 10
                else:
                    continue
            except:
                print(entry)


            oneRecord = {"licensePlate": licensePlate, "latitude": latitude,
                         "longitude": longitude, "timeRecorded": timeInNumber}
            records.append(oneRecord)
    print(len(records))
    result = db.shenzhenTaxis.insert(records)
