import board
import digitalio
import time
import pwmio
from adafruit_motor import servo

led = digitalio.DigitalInOut(board.GP1)         #Initializing led pins and outputs
led.direction = digitalio.Direction.OUTPUT      
led2= digitalio.DigitalInOut(board.GP2)
led2.direction = digitalio.Direction.OUTPUT

button= digitalio.DigitalInOut(board.GP3)       #Initializing button pins and input
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

pwm_servo = pwmio.PWMOut(board.GP4, duty_cycle=2 ** 15, frequency=50)   #Initializing
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo1.angle = 0

while button.value == False:
    print("ready for liftoff")


for x in range (10):                            #prints numbers 1-10 in ascending order
    print(10-x)                                 #changes to print numbers 1-10 in descending order
    led.value = True                            #blinks on and off every second
    time.sleep(.5)
    led.value = False
    time.sleep(.5)

print ("liftoff")
while True:                                     #Need a loop to continue running code after for loop
    led2.value = True                           #Turns on green led after countdown
    servo1.angle = 180
    time.sleep(5)
    led2.value = True
    