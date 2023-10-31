'''
Author: Hassaan Ahmed
Date: August 10, 2023
'''
# Imports
import numpy as np
from pygame import mixer
import time
import cv2
from tkinter import *
import tkinter.messagebox
import sqlite3
import time
import subprocess
import os

# Initialize Tkinter
root = Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
window_height = 650
window_width = 1240
window_x = (root.winfo_screenwidth() // 2) - (window_width // 2)
window_y = (root.winfo_screenheight() // 4) - (window_height // 4)

root.geometry('{}x{}+{}+{}'.format(window_width, window_height, window_x, window_y))

# Create main frame
main_frame = Frame(root, relief=RIDGE, borderwidth=2)
main_frame.pack(fill=BOTH, expand=1)
root.title('Drowsiness Monitoring System')
main_frame.config(background='black')

# Title Label
title_label = Label(main_frame, text="Drowsiness Monitoring System", bg='black', fg="white", font=('Times 25 bold'))
title_label.pack(side=TOP)

# Background Image
background_image = PhotoImage(file="./assets/image_1.png")
background_label = Label(main_frame, image=background_image)
background_label.pack(side=TOP)

# Get user email from file
with open("./Database/user_email.txt", "r") as email_file:
    user_email = email_file.read().strip()

# Define close window behavior
def close_window():
    root.destroy()

root.protocol('WM_DELETE_WINDOW', close_window)

# Define program exit
def exit_program():
    exit()

# Your functions go here...
def alert_sound():
    mixer.init()
    alert = mixer.Sound('beep-07.wav')
    alert.play()
    time.sleep(0.1)
    alert.play()


def alarm_sound():
    mixer.init()
    alarm = mixer.Sound('alarm.wav')
    alarm.play()
    time.sleep(2)
    alarm.play()

# Detect and Record button
def webcam_detection_record():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
    eye_glasses_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    timestamp1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter(f'{user_email}_({time.time()}).avi', fourcc, 9.0, (640, 480))

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(frame, 'Face', (x + w, y + h), font, 1, (250, 250, 250), 2, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            eye_g = eye_glasses_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eye_g:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        output.write(frame)
        cv2.namedWindow("Frame", cv2.WINDOW_GUI_NORMAL)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)

        if key == 27:  # Press 'Esc' key to exit the loop
            break

    output.release()
    cap.release()
    cv2.destroyAllWindows()

# Drowsiness Detection button
def blink_detection():
    conn = sqlite3.connect("./Database/AccountSystem.db")
    cursor = conn.cursor()

    cursor.execute('''
       CREATE TABLE IF NOT EXISTS screenshots (
          id INTEGER PRIMARY KEY,
          filename TEXT,
          timestamp DATETIME
       )
    ''')
    conn.commit()

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    blink_cascade = cv2.CascadeClassifier('CustomBlinkCascade.xml')
    timestamp1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter(f'{user_email}_({time.time()}).avi', fourcc, 9.0, (640, 480))
    count = 0

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(frame, 'Face', (x + w, y + h), font, 1, (250, 250, 250), 2, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            blinks = blink_cascade.detectMultiScale(roi_gray)
            if len(blinks) == 0:
                count = 0
            for (ebx, eby, ebw, ebh) in blinks:
                count += 1
                score = str(count)
                cv2.putText(frame, "Drowsiness Score: " + score, (10, 30), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.rectangle(roi_color, (ebx, eby), (ebx + ebw, eby + ebh), (255, 255, 0), 2)

                if score == "5":
                    alert_sound()
                elif score == "40":
                    screenshot_filename = f"{user_email}({time.time()}).png"
                    cv2.imwrite(screenshot_filename, frame)

                    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                    cursor.execute('INSERT INTO screenshots (filename, timestamp) VALUES (?, ?)',
                                   (screenshot_filename, timestamp))
                    conn.commit()
                    alarm_sound()

        output.write(frame)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)

        if key == 27:
            break

    output.release()
    cap.release()
    cv2.destroyAllWindows()

# Reports button
def view_reports():
    subprocess.run(["python", "checkReports.py"])

# User Management button (only available for admin)
def manage_users():
    subprocess.run(["python", "manage.py"])

# Logout button
def logout_user():
    subprocess.Popen(["python", "account_system.py"])
    with open("./Database/user_email.txt", "w") as file:
        pass
    os._exit(0)

# Buttons
detect_record_button = Button(main_frame, padx=5, pady=5, width=39, bg='white', fg='black', relief=GROOVE,
                             command=webcam_detection_record, text='Detect & Record', font=('helvetica 15 bold'))
detect_record_button.place(x=370, y=104)

drowsiness_detection_button = Button(main_frame, padx=5, pady=5, width=39, bg='white', fg='black', relief=GROOVE,
                                     command=blink_detection, text='Drowsiness Detection', font=('helvetica 15 bold'))
drowsiness_detection_button.place(x=370, y=176)

if user_email == "admin":
    user_management_button = Button(main_frame, padx=5, pady=5, width=39, bg='black', fg='white', relief=GROOVE,
                                    text='User Management', command=manage_users, font=('helvetica 15 bold'))
    user_management_button.place(x=370, y=324)

reports_button = Button(main_frame, padx=5, pady=5, width=39, bg='black', fg='white', relief=GROOVE,
                        text='Previous Detected Images', command=view_reports, font=('helvetica 15 bold'))
reports_button.place(x=370, y=250)

logout_button = Button(main_frame, padx=5, pady=5, width=39, bg='black', fg='white', relief=GROOVE,
                       text='Logout', command=logout_user, font=('helvetica 15 bold'))
logout_button.place(x=370, y=600)

# Start the main event loop
root.mainloop()
