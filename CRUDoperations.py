from pymongo import MongoClient

client = MongoClient()
db = client.testDB  # name of database: 'testDB'

illegalTime = db.shenzhenTaxis.find({'timeRecorded':{"$lt":1451664000}})
print(illegalTime.count())
db.shenzhenTaxis.remove({'timeRecorded':{"$lt":1451664000}})
print('Cleaning completed.')
print(db.shenzhenTaxis.find().count())