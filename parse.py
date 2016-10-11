import json
import time
import datetime

trajectoryArray = []
carsArray = []
with open ("GPS_2016_01_02",'r') as file:
    while True :
        entry = file.readline()
        if (entry == ""):
            break
        else:
            carsArray.append(entry[0:7])
            if(len(carsArray)%10000 == 0):
                print (len(carsArray))
    print('There are ', len(set(carsArray)), ' cars.')



    '''
            if entry[0:7] == '粤B0U0R3':
                #print (entry)
                print('['+ entry[19:28]+ ', '+entry[8:18] + '],')
                oneLatitudeLongitude = '['+ entry[19:28]+ ', '+entry[8:18] + '],'
                timeNow = entry[29:48]
                unixTimestamp = time.mktime(datetime.datetime.strptime(timeNow, "%Y-%m-%d %X").timetuple()) *1000
                trajectoryArray.append({"licensePlate":entry[0:7],"latitude":float(entry[19:28]),
                                        "longitude":float(entry[8:18]), "timeRecorded": { "$date": unixTimestamp }})
                oneRecord = {"licensePlate":entry[0:7],"latitude":float(entry[19:28]),
                                        "longitude":float(entry[8:18]), "timeRecorded": { "$date": unixTimestamp }}
                #print(oneRecord)
                #with open('粤B0U0R3.json', 'a') as outfile:
                    #json.dump(oneRecord, outfile)
                with open('allLatitudeLongitude.json','a') as outfile:
                    json.dump(oneLatitudeLongitude,outfile)
    '''



