import os, pickle
import face_recognition
import numpy as np

DB_FILE = "known_faces.pkl"
TOLERANCE = 0.5

def load_db():
    if not os.path.exists(DB_FILE):
        return [], []
    with open(DB_FILE, "rb") as f:
        data = pickle.load(f)
    return data["encodings"], data["names"]

def save_db(encodings, names):
    with open(DB_FILE, "wb") as f:
        pickle.dump({"encodings": encodings, "names": names}, f)

def enroll_face(img_rgb, name):
    encs = face_recognition.face_encodings(img_rgb)
    if not encs:
        return False
    encodings, names = load_db()
    encodings.extend(encs)
    names.extend([name] * len(encs))
    save_db(encodings, names)
    return True

def recognize_face(face_rgb):
    encodings, names = load_db()
    if not encodings:
        return None
    face_encs = face_recognition.face_encodings(face_rgb)
    if not face_encs:
        return None
    enc = face_encs[0]
    distances = face_recognition.face_distance(encodings, enc)
    best_idx = np.argmin(distances)
    if distances[best_idx] <= TOLERANCE:
        return names[best_idx]
    return None
