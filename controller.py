import time
try:
    import RPi.GPIO as GPIO
    ON_PI = True
except ImportError:
    ON_PI = False

GREEN = 17
RED   = 27
LOCK  = 22

def setup():
    if ON_PI:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GREEN, GPIO.OUT)
        GPIO.setup(RED, GPIO.OUT)
        GPIO.setup(LOCK, GPIO.OUT)
        GPIO.output(GREEN, GPIO.LOW)
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(LOCK, GPIO.LOW)

def cleanup():
    if ON_PI:
        GPIO.cleanup()

def access_granted(duration=3):
    if ON_PI:
        GPIO.output(GREEN, GPIO.HIGH)
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(LOCK, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(GREEN, GPIO.LOW)
        GPIO.output(LOCK, GPIO.LOW)
    else:
        print("[SIM] GREEN ON → Access granted")

def access_denied(duration=2):
    if ON_PI:
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(GREEN, GPIO.LOW)
        time.sleep(duration)
        GPIO.output(RED, GPIO.LOW)
    else:
        print("[SIM] RED ON → Access denied")
