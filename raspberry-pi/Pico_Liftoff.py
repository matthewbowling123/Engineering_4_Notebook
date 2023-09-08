import time
import board
import digitalio

LED1 = digitalio.DigitalInOut(board.GP0)
LED1.direction = digitalio.Direction.OUTPUT
LED2 = digitalio.DigitalInOut(board.GP1)
LED2.direction = digitalio.Direction.OUTPUT
for x in range(10):
    launch = 10-x
    print(launch)
    LED1.value = True
    time.sleep(.5)
    LED1.value = False
    time.sleep(.5)
print("Liftoff")
LED2.value = True
time.sleep(5)
LED2.value = False