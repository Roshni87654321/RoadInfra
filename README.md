# RoadGuardian AI

## Overview

RoadGuardian AI is a Flask-based web application that detects potholes from uploaded road videos using a trained YOLO model. Once road damage is detected, the application stores the detection details in a SQLite database, displays the location on an interactive map, and sends an email notification to the concerned authority.

---

## Features

- Upload road videos
- Detect potholes using YOLO
- Store detection details in SQLite
- Display road location using Leaflet and OpenStreetMap
- Send email notifications through Gmail SMTP

---

## Technologies Used

- Python
- Flask
- YOLO (Ultralytics)
- OpenCV
- SQLite
- HTML
- Leaflet.js
- OpenStreetMap

---

## Project Structure

```
RoadInfra/
│
├── backend/
│   ├── app.py
│   ├── detector.py
│   ├── database.py
│   └── email_sender.py
│
├── models/
│   └── best.pt
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── roadguardian.db
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## Installation


pip install -r requirements.txt
```

---

## YOLO Model

The trained YOLO model is already included in the repository.

```
models/
    best.pt
```

No additional downloads are required.

If you wish to use another trained model, replace `best.pt` and update the model path in `backend/detector.py`.

---

## Gmail Configuration

The application sends email notifications using Gmail SMTP.

### Step 1

Enable **2-Step Verification** for your Google account.

```
https://myaccount.google.com/security
```

### Step 2

Generate an App Password.

```
https://myaccount.google.com/apppasswords
```

Enter an application name such as

```
RoadGuardian
```

Google will generate a 16-character App Password.

### Step 3

Create a `.env` file in the project root.

```env
SENDER_EMAIL=yourgmail@gmail.com
APP_PASSWORD=your16characterapppassword
```

Do not use your Gmail account password. Use the generated App Password.

---

## Running the Project


## Application Workflow

```
Upload Road Video
        │
        ▼
YOLO detects potholes
        │
        ▼
Detection stored in SQLite
        │
        ▼
Email notification sent
        │
        ▼
Location displayed on the map
```

---

## Database

The application uses SQLite.

Each detection stores:

- Video name
- Number of potholes detected
- Latitude
- Longitude

---

## Map

The current implementation uses predefined coordinates for demonstration.

```
Latitude : 17.3850

Longitude : 78.4867
```

In a production environment, these coordinates would be obtained from the GPS location of the device used to upload the video.

---

## Email Notification

After every successful detection, an email is automatically sent containing:

- Video name
- Number of potholes detected
- Latitude
- Longitude

The current implementation sends the email to the configured Gmail account. In a production deployment, this can be changed to send notifications directly to the appropriate municipal authority.

---

## Notes

- Ensure the `best.pt` model remains inside the `models` directory.
- A Gmail App Password is required for email functionality.
- The current version uses predefined coordinates for demonstration purposes.

---

## Future Scope

- Live GPS integration
- Real-time road monitoring
- Detection of multiple road defects
- Mobile application support
- Government monitoring dashboard
- Cloud database integration
- Automatic maintenance request generation