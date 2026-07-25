import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Read email and app password from .env
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")


def send_email(video_name, potholes, latitude, longitude):

    subject = "🚧 Road Damage Alert"

    body = f"""
Road Damage Detection Report

Video Name: {video_name}

Potholes Detected: {potholes}

Latitude: {latitude}

Longitude: {longitude}

Please inspect the road as soon as possible.

Regards,
RoadGuardian AI
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = SENDER_EMAIL

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(SENDER_EMAIL, APP_PASSWORD)

        server.send_message(msg)

        server.quit()

        print("✅ Email Sent Successfully!")

    except Exception as e:
        print("❌ Email Failed!")
        print(e)