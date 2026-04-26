import random
import time
from datetime import datetime
from pymongo import MongoClient

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://chaitanya_db_user:fcc12345@fcc-cluster.8pbu5ea.mongodb.net/")
db = client["iot_database"]
collection = db["sensor_readings"]

# 3 simulated sensors
SENSORS = ["Sensor-1", "Sensor-2", "Sensor-3"]

print("🚀 IoT Simulator started. Sending data every 3 seconds...")

while True:
    for sensor_id in SENSORS:
        reading = {
            "sensor_id": sensor_id,
            "temperature": round(random.uniform(22.0, 38.0), 2),
            "humidity": round(random.uniform(40.0, 90.0), 2),
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        }
        collection.insert_one(reading)
        print(f"✅ {reading['sensor_id']} → Temp: {reading['temperature']}°C | Humidity: {reading['humidity']}%")
    
    time.sleep(3)