import time
import board
import digitalio


for x in range(10):
    launch = 10-x
    print(launch)
    time.sleep(1)

if launch == 1:
    print("Liftoff")