# Drowsiness-Detection-System

Table of Contents
Introduction
Features
Technologies Used
Getting Started
Usage
Screenshots
Contributing
License

Introduction
The Drowsiness Detection application is a desktop-based solution designed to monitor user fatigue levels and ensure their safety, particularly while engaged in tasks that require attentiveness, such as driving or operating heavy machinery.

The application features two distinct panels: one for the user and another for the admin. In the user section, individuals can log in and activate their camera. The system utilizes facial and eye detection to monitor blinking patterns. When a user exhibits signs of drowsiness, the application emits a short beep. If drowsiness persists, an alarm will sound to awaken the user. Additionally, a screenshot is captured and stored in an SQL database, allowing users to review their past records.

In the admin section, administrators have access to user management and record management functionalities, in addition to the standard user features.

Features
User-friendly GUI powered by Tkinter for easy interaction.
Real-time facial and eye detection using OpenCV's Haar cascades.
Alerts for short and prolonged periods of drowsiness.
Continuous monitoring and alarm activation to prevent accidents.
Secure user authentication and record management.
Screenshot capture and SQL database integration for record storage.
Intuitive admin panel with user and record management capabilities.
Technologies Used
OpenCV
Haarcascade
Tkinter
SQLite
[Add more technologies used]
Getting Started
To get started with the Drowsiness Detection application, follow these steps:

Clone the repository to your local machine.
bash
Copy code
git clone https://github.com/yourusername/drowsiness-detection.git
Install the required dependencies using Pip.
bash
Copy code
pip install -r requirements.txt
[Add any specific setup or configuration steps]
Usage
Navigate to the project directory.
bash
Copy code
cd drowsiness-detection
Launch the application by running the main script.
bash
Copy code
python main.py
[Provide a brief usage guide for users and admins]
Screenshots
[Include screenshots or GIFs showcasing the application]

Contributing
[Explain how others can contribute to your project]

License
[Specify the license under which your project is released]

[Include any necessary disclaimers or notices]

Thank you for using the Drowsiness Detection Application!

For any questions or feedback, please open an issue.

[Optional: Add badges for license, stars, forks, etc.]

Back to Top
