import os
from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://chaitanya_db_user:fcc12345@fcc-cluster.8pbu5ea.mongodb.net/")

client = MongoClient(MONGO_URI)
db = client["iot_database"]
collection = db["sensor_readings"]

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/data")
def get_data():
    readings = list(collection.find({}, {"_id": 0}).sort("timestamp", -1).limit(20))
    return jsonify(readings)

@app.route("/api/latest")
def get_latest():
    sensors = ["Sensor-1", "Sensor-2", "Sensor-3"]
    latest = []
    for sensor in sensors:
        reading = collection.find_one({"sensor_id": sensor}, {"_id": 0}, sort=[("timestamp", -1)])
        if reading:
            latest.append(reading)
    return jsonify(latest)

if __name__ == "__main__":
    app.run(debug=True)