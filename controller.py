import RPi.GPIO as GPIO
import time

# Pin numbers (BCM mode)
GREEN_LED = 17   # Green LED → Access Granted
RED_LED   = 27   # Red LED   → Access Denied

def setup():
    """Setup GPIO pins."""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GREEN_LED, GPIO.OUT)
    GPIO.setup(RED_LED, GPIO.OUT)
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(RED_LED, GPIO.LOW)

def access_granted():
    """Turn on green LED (Access Granted)."""
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(GREEN_LED, GPIO.LOW)

def access_denied():
    """Turn on red LED (Access Denied)."""
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(RED_LED, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(RED_LED, GPIO.LOW)

def cleanup():
    """Reset GPIO pins when exiting."""
    GPIO.cleanup()
