# lock_test.py
import controller
import time

controller.setup()

print("Green (Access Granted)")
controller.access_granted()
time.sleep(1)

print("Red (Access Denied)")
controller.access_denied()
time.sleep(1)

controller.cleanup()
print("Done.")
