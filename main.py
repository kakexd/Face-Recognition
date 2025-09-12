from faces import recognize_face
import lock_control
import cv2, sys, numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QSlider
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, Qt

# Camera setup
s_index, e_index = 0, 3
cameras, face_cascade = [], cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
for index in range(s_index, e_index + 1):
    cap = cv2.VideoCapture(index)
    if cap.isOpened(): cameras.append(cap)
    else: cap.release()
if not cameras:
    print("No cameras found. Exiting...")
    sys.exit(-1)

class MultiCameraApp(QMainWindow):
    def __init__(self):
        super().__init__()
        lock_control.setup()
        self.allowed = {"YourName"}  # enrolled users

        # Layout setup
        self.setWindowTitle("Face Recognition Lock")
        self.setGeometry(50, 50, 900, 600)
        self.central_widget, self.layout = QWidget(), QGridLayout()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.layout)

        self.video_labels, self.timers, self.captures = [], [], cameras
        for i, cap in enumerate(self.captures):
            labels = [QLabel(self) for _ in range(4)]
            for col, label in enumerate(labels):
                label.setScaledContents(True)
                self.layout.addWidget(label, i, col)
            self.video_labels.append(labels)
            timer = QTimer(self)
            timer.timeout.connect(lambda i=i: self.update_frame(i))
            timer.start(30)
            self.timers.append(timer)

        self.cameras_active = True

    def update_frame(self, index):
        ret, frame = self.captures[index].read()
        if not self.cameras_active or not ret: return
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:
            face_crop = frame[y:y+h, x:x+w]
            face_rgb = cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB)
            name = recognize_face(face_rgb)

            if name and name in self.allowed:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
                cv2.putText(frame, f"Access Granted: {name}", (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
                lock_control.access_granted()
            else:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)
                cv2.putText(frame, "Access Denied", (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
                lock_control.access_denied()

        display_frames = [frame, cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB), frame, cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)]
        for view_index, img in enumerate(display_frames):
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = img.shape
            q_img = QImage(img.data, w, h, 3*w, QImage.Format_RGB888)
            self.video_labels[index][view_index].setPixmap(QPixmap.fromImage(q_img))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MultiCameraApp()
    window.show()
    try:
        sys.exit(app.exec_())
    finally:
        lock_control.cleanup()
