# Face-Recognition

# REQUIREMENTS

Raspberry Pi (3B/4 recommended)

Pi Camera module or USB camera

2 LEDs (Red & Green)

2 × 220Ω resistors

Breadboard + jumper wires

Optional: Relay/servo for a mechanical lock

# Instructions
1. enroll your face:
   - python3 enroll.py

2. Launch the GUI:
   - python3 main.py

3. Observe the outcome.


# How it works?

Opens the default camera (/dev/video0).

Detects faces using Haar cascades.

Crops each face → checks against your enrolled database (known_faces.pkl).

If recognized → Green LED + lock relay.

If not recognized or no face detected → Red LED.

Runs in a loop until you stop it with CTRL+C.

# ~ Troubleshooting ~

## Option 1.
In case of hash mismatch -> add the website into --trusted-host
  - python3 -m pip install --trusted-host pip -YOUR-PACKAGE-

Your pip command may have downloaded a corrupted file.

## Option 2.
Try again with disabling cache:
 pip install --no-cache-dir face_recognition.

## Option 3.
Try again without hash check (bypass the hash security): pip install face_recognition --no-deps

No camera detected → Check USB / enable Pi Camera in raspi-config.

face_recognition install fails → You may need to build dlib manually.

LEDs not working → Double-check GPIO wiring and pins in lock_control.py.

GUI too slow → Try running headless (without PyQt5) for performance.

This version avoids PyQt5 entirely, so it uses much less CPU/RAM and is more suitable for a real lock system.

Would you like me to also add a logging system (e.g., save access attempts with timestamp + result into a text file or CSV)? That way, you’d have an audit trail of who tried to open the lock.

# ~ Optional ~
run:
python3 headless_main.py
