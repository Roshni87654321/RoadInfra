from flask import Flask, render_template, request
import os

from detector import detect_potholes
from database import init_db, save_detection
from email_sender import send_email

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates")
)

# Upload folder
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize database
init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_video():

    if "video" not in request.files:
        return "No video selected."

    video = request.files["video"]

    if video.filename == "":
        return "Please choose a video."

    # Save uploaded video
    filepath = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(filepath)

    # Detect potholes
    potholes = detect_potholes(filepath)

    # Dummy coordinates (Hyderabad)
    latitude = 17.3850
    longitude = 78.4867

    # Save to database
    save_detection(
        video.filename,
        potholes,
        latitude,
        longitude
    )

    # Send email
    send_email(
        video.filename,
        potholes,
        latitude,
        longitude
    )

    # Send data back to HTML
    return render_template(
        "index.html",
        status="Detection Completed",
        potholes=potholes,
        latitude=latitude,
        longitude=longitude,
        email_status="Email Sent Successfully"
    )


if __name__ == "__main__":
    app.run(debug=True)