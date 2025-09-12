import cv2
from faces import recognize_face
import lock_control
import time

def run():
    lock_control.setup()
    allowed = {"YourName"}  # replace with your enrolled name
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ No camera found. Exiting...")
        return

    print("📷 Camera started. Press CTRL+C to quit.")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("⚠️ Frame not captured. Retrying...")
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray, 1.1, 5)

            if len(faces) == 0:
                # No face detected → Access denied
                lock_control.access_denied()
                continue

            for (x, y, w, h) in faces:
                face_crop = frame[y:y+h, x:x+w]
                face_rgb = cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB)
                name = recognize_face(face_rgb)

                if name and name in allowed:
                    print(f"✅ Access Granted for {name}")
                    lock_control.access_granted()
                else:
                    print("❌ Access Denied")
                    lock_control.access_denied()

            time.sleep(0.5)  # reduce CPU load

    except KeyboardInterrupt:
        print("\n🛑 Exiting...")

    finally:
        cap.release()
        lock_control.cleanup()
        print("🔌 GPIO cleaned up.")

if __name__ == "__main__":
    run()
