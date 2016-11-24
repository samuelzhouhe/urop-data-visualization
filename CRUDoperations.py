from pymongo import MongoClient
import pymongo
import geopy
from geopy.distance import VincentyDistance

client = MongoClient()
db = client.testDB  # name of database: 'testDB'
print(db.shenzhenTaxis.find().count())
# db.shenzhenTaxis.create_index([("latitute", pymongo.ASCENDING)])
# db.shenzhenTaxis.create_index([("longitude", pymongo.ASCENDING)])




# transfer the data near Futian CBD to a new collection
futianCenter = geopy.Point(22.543, 114.055)
northLat = VincentyDistance(kilometers=2).destination(futianCenter, 0).latitude
southLat = VincentyDistance(kilometers=2).destination(futianCenter, 180).latitude
eastLon = VincentyDistance(kilometers=2).destination(futianCenter, 90).longitude
westLon = VincentyDistance(kilometers=2).destination(futianCenter, 270).longitude
print(northLat, southLat, eastLon, westLon)

transferCondition = {"latitude": {"$gt": southLat, "$lt": northLat}, "longitude": {"$gt": westLon, "$lt": eastLon},
                     'licensePlate': "粤BL9029"}
# transferCondition = {'licensePlate':'粤BL9029'}
'''print("Now searching database for: " , transferCondition)
resultCursor = db.shenzhenTaxis.find(transferCondition)
toTransfer = []
for document in resultCursor:
    print(document)
    toTransfer.append(document)
result = db.futian.insert(toTransfer)
print(db.futian.find().count())'''
db.shenzhenTaxis.aggregate([{'$match': transferCondition}, {'$out': "futian"}])
