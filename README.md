# Face Recognition Project

This project is a Python-based application for face recognition using the `face-recognition` library. It is designed to recognize faces in images or video streams and can be integrated with Firebase for data storage and retrieval.

## Features

- Face detection and recognition in images and video streams.
- Integration with Firebase Firestore and Storage for data management.
- Easy-to-use command-line interface for setup and execution.
- Customizable `.gitignore` file for Python projects.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)

## Setup Instructions for Virtual Environment:

- Run the setup.bat script to automate the setup process:

    - It will create virtualenv .venv

    - Activates the virtual environment.
    - Upgrades pip to the latest version.
    - Installs all dependencies listed in requirements.txt.
    - Create .gitignore file

1. **Clone the Repository** (if not already cloned):
   ```bash
   git clone https://github.com/mnoukhej/FaceRecognition.git
   cd FaceRecognition


##  Project Structure
FaceRecognition/
├── Images/                  # Folder containing images for face recognition
├── Resources/               # Additional resources (if any)
├── .gitignore               # Git ignore file
├── AddDataToDatabase.py     # Script to add data to Firebase database
├── EncodeFile.p             # Encoded face data file
├── EncodeGenerator.py       # Script to generate face encodings
├── README.md                # This file
├── main.py                  # Main application script
├── requirements.txt         # List of dependencies
├── serviceAccountKey.json   # Firebase service account key (not included in the repo)
├── setup.bat                # Setup script for Windows
└── run_server.bat           # Script to run the application