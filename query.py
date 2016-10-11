import pymongo
from pymongo import MongoClient
from flask import Flask, request, jsonify

client = MongoClient()
db = client.testDB  # name of database: 'testDB'


print(db.shenzhenTaxis.count())

cursor = db.shenzhenTaxis.find(    {  "latitude": { "$lt": 22.545 } }          )
print(cursor.count())
# db.shenzhenTaxis.create_index([("timeRecorded",pymongo.ASCENDING)])




app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello world'}), 404

@app.route('/queryFromDB',methods=['POST'])
def queryFromDB():
    requestDetail = request.json
    resultCursor = db.shenzhenTaxis.find(requestDetail)
    queryResult = []
    for document in resultCursor:
        licensePlate = document.get('licensePlate')
        latitude = document.get('latitude')
        longitude = document.get('longitude')
        timeRecorded = document.get('timeRecorded')
        oneResult = {'licensePlate':licensePlate,'latitude':latitude,'longitude':longitude,'timeRecorded':timeRecorded}
        queryResult.append(oneResult)
    return jsonify(queryResult),200


app.run('127.0.0.1','4000')
print("Running on localhost:4000")