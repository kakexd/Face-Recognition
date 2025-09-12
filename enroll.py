import cv2
from faces import enroll_face

name = input("Enter your name: ").strip()
cap = cv2.VideoCapture(0)
print("Press SPACE to capture face, ESC to exit.")
while True:
    ret, frame = cap.read()
    if not ret: break
    cv2.imshow("Enrollment", frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27: break
    if k == 32:  # SPACE
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if enroll_face(rgb, name):
            print("Enrolled successfully.")
        else:
            print("No face detected, try again.")
cap.release()
cv2.destroyAllWindows()
