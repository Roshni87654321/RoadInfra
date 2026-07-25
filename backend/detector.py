from ultralytics import YOLO
import cv2

# Load the trained model only once
model = YOLO("models/best.pt")


def detect_potholes(video_path):

    cap = cv2.VideoCapture(video_path)

    pothole_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame)

        for result in results:

            boxes = result.boxes

            pothole_count += len(boxes)

    cap.release()

    return pothole_count