import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP1)         # This sets up the pins for the LED and Buttons.
led.direction = digitalio.Direction.OUTPUT      
led2= digitalio.DigitalInOut(board.GP2)
led2.direction = digitalio.Direction.OUTPUT
button= digitalio.DigitalInOut(board.GP3)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

while button.value == False:
    print("ready for liftoff")


for x in range (10):                            #Print 10-1
    print(10-x)                                
    led.value = True                            #blinks on and off every second
    time.sleep(.5)
    led.value = False
    time.sleep(.5)

print ("liftoff")
while True:                                     #Need a loop to continue running code after for loop
    led2.value = True                           #Turns on green led after countdown
    time.sleep(5)
    led2.value = True