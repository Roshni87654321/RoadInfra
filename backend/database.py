import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "roadguardian.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detections(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        video_name TEXT,
        potholes INTEGER,
        latitude REAL,
        longitude REAL,
        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_detection(video_name, potholes, latitude, longitude):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO detections(video_name,potholes,latitude,longitude)
    VALUES(?,?,?,?)
    """,(video_name,potholes,latitude,longitude))

    conn.commit()
    conn.close()