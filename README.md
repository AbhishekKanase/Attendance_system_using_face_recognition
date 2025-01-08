# Face Recognition Attendance System

This is a Python-based project that utilizes face recognition technology to automate attendance tracking. The system captures video from a webcam or IP camera, identifies individuals in real-time, and logs their attendance into a CSV file with a timestamp.

## Features

- Detects and recognizes faces in real-time using the `face_recognition` library.
- Automatically logs attendance with the person's name and time.
- Supports integration with a webcam or IP camera.
- Exports attendance data to a CSV file for easy record-keeping.

## Technologies Used

- Python
- OpenCV
- `face_recognition` library
- NumPy
- CSV for data storage

## Setup and Installation

### Prerequisites

1. Install Python 3.8 or later.
2. Install the required Python libraries:

   ```bash
   pip install face_recognition opencv-python numpy
   ```

3. Install [dlib](http://dlib.net/) (a dependency for `face_recognition`). On some systems, you may need to install additional build tools:

   ```bash
   # For Linux
   sudo apt-get install cmake

   # For macOS
   brew install cmake

   # For Windows
   choco install cmake
   ```

### Steps to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/face-recognition-attendance.git
   cd face-recognition-attendance
   ```

2. Place the reference images of individuals to be recognized in the `photos/` directory. Each image should have a clear view of the face and be named appropriately (e.g., `messi.JPG`, `rock.JPG`).

3. Run the script:

   ```bash
   python attendance_system.py
   ```

4. The system will:
   - Capture video from the default webcam or IP camera.
   - Detect and recognize faces based on the provided reference images.
   - Log attendance data to a CSV file named with the current date (e.g., `2025-01-08.csv`).

5. Press `q` to exit the application.

## Configuration

### IP Camera Setup

If using an IP camera, update the `address` variable in the script with your camera's streaming URL:

```python
address = "http://<your-ip>:<port>/video"
```

### Adding New Faces

1. Add a new image to the `photos/` directory.
2. Load and encode the new image in the script:

   ```python
   new_person_image = face_recognition.load_image_file("photos/new_person.JPG")
   new_person_encoding = face_recognition.face_encodings(new_person_image)[0]
   known_face_encoding.append(new_person_encoding)
   known_faces_names.append("new_person")
   ```

## Limitations

- Performance may degrade with a large number of faces to recognize.
- Proper lighting and camera quality significantly impact recognition accuracy.
- The system does not handle situations where multiple people have similar facial features.

## Future Enhancements

- Add support for storing attendance data in a database.
- Create a user-friendly web or GUI interface.
- Implement periodic updates for reference images.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- [face_recognition](https://github.com/ageitgey/face_recognition) library for the face detection and recognition functionality.
- OpenCV for video processing.

## Contact

For any questions or issues, feel free to open an issue on GitHub or contact [abhishekanase07@gmail.com].

