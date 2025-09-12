# REQUIREMENTS

Raspberry Pi (3B/4 recommended)

Pi Camera module or USB camera

2 LEDs (Red & Green)

2 × 220Ω resistors

Breadboard + jumper wires

Optional: Relay/servo for a mechanical lock


# Install Dependencies
These are dependencies for the project:

``` sudo apt install -y python3-pip build-essential cmake libatlas-base-dev libjpeg-dev ```

``` pip3 install opencv-python face-recognition PyQt5 RPi.GPIO numpy dlib ```

Just in case, increase the operation system to use portion of the disk as virtual memory in case if RAM is exhausted.

``` sudo nano /etc/dphys-swapfile ```

Scroll down to the configuration which reads in example:
CONF_SWAPSIZE=100 -> CONF_SWAPSIZE=1024

And then update it to use 1024MB rather than 100MB:

After you have updated the ```/etc/dphys-swapfile file```, run the following two commands to restart the swap service:

``` sudo /etc/init.d/dphys-swapfile stop ```

``` sudo /etc/init.d/dphys-swapfile start ```

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
 pip install --no-cache-dir face-recognition.

## Option 3.
Try again without hash check (bypass the hash security): pip install face-recognition --no-deps

# If packages are installed and working properly:
No camera detected → Check USB / enable Pi Camera in raspi-config.

face-recognition install fails → You may need to build dlib manually. **Check option 3.**

LEDs not working → Double-check GPIO wiring and pins in lock_control.py.
via Terminal use: ```pinout```

GUI too slow → Try running headless (without PyQt5) for performance.

This version avoids PyQt5 entirely, so it uses much less CPU/RAM and is more suitable for a real lock system.

Would you like me to also add a logging system (e.g., save access attempts with timestamp + result into a text file or CSV)? That way, you’d have an audit trail of who tried to open the lock.

# ~ Optional ~
run:
python3 headless_main.py


# DOCX

``` sudo apt-get install build-essential cmake ```
 
``` sudo apt-get install libgtk-3-dev ```
 
``` sudo apt-get install libboost-all-dev ```
