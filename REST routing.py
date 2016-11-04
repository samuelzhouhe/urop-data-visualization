import pymongo
from pymongo import MongoClient
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

client = MongoClient()
db = client.testDB  # name of database: 'testDB'

print(db.shenzhenTaxis.count())


db.shenzhenTaxis.create_index([("timeRecorded", pymongo.ASCENDING)])

app = Flask(__name__)
CORS(app)

#Hello world routing
@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello world'}), 200

#Any query from the entire database
@app.route('/queryFromDB', methods=['POST'])
def queryFromDB():
    requestDetail = request.json
    print(requestDetail)
    resultCursor = db.shenzhenTaxis.find(requestDetail)
    queryResult = []
    for document in resultCursor:
        licensePlate = document.get('licensePlate')
        latitude = document.get('latitude')
        longitude = document.get('longitude')
        timeRecorded = document.get('timeRecorded')
        oneResult = {'licensePlate': licensePlate, 'latitude': latitude, 'longitude': longitude,
                     'timeRecorded': timeRecorded}
        queryResult.append(oneResult)
    return jsonify(queryResult), 200

#Returns the earliest and latest recorded time
@app.route('/getTimeRange', methods=['GET'])
def getTimeRange():

    smallest = db.shenzhenTaxis.find({'timeRecorded':{"$gt":1451664000}}).sort([("timeRecorded", 1)])
    legitTime = db.shenzhenTaxis.find({'timeRecorded':{"$gt":1451664000}})
    print(legitTime.count())
    # for doc in smallest:
    #     earliest = doc.get('timeRecorded')
    #     print(earliest)
    result = {'earliest':0,'latest':0}
    return jsonify(result), 200

app.run('127.0.0.1', '4000')
print("Running on localhost:4000")
