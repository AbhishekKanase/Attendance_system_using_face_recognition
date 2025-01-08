import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# Initialize video capture
video_capture = cv2.VideoCapture(0)

# IP Camera Address
address = "http://10.154.4.34:8080/video"
video_capture.open(address)

# Load and encode known faces
messi_image = face_recognition.load_image_file("photos/messi.JPG")
messi_encoding = face_recognition.face_encodings(messi_image)[0]

rock_image = face_recognition.load_image_file("photos/rock.JPG")
rock_encoding = face_recognition.face_encodings(rock_image)[0]

ronaldo_image = face_recognition.load_image_file("photos/ronaldo.JPG")
ronaldo_encoding = face_recognition.face_encodings(ronaldo_image)[0]

# Define known face encodings and names
known_face_encoding = [messi_encoding, rock_encoding, ronaldo_encoding]
known_faces_names = ["messi", "rock", "ronaldo"]

# Copy of student names for attendance
students = known_faces_names.copy()

# Initialize variables
face_locations = []
face_encodings = []
face_names = []
frame_skip = True

# Create CSV file for attendance
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
f = open(current_date + '.csv', 'w+', newline='')
lnwriter = csv.writer(f)

while True:
    # Read video frame
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to capture frame. Exiting.")
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if frame_skip:
        # Detect face locations and encodings
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []

        for face_encoding in face_encodings:
            # Compare detected face to known faces
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name = known_faces_names[best_match_index]

            face_names.append(name)

            if name in known_faces_names and name in students:
                students.remove(name)
                print(f"Marked attendance for: {name}")
                # Update time dynamically
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                lnwriter.writerow([name, current_time])

    # Display the video frame
    cv2.imshow("Attendance System", frame)

    # Exit loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()
f.close()
