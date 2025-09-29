from machine import Pin
import time

# Set up LED on GPIO 15
led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(13, Pin.OUT)

while True:
    led1.on()         # turn LED on
    print("LED 1 on")
    time.sleep(1)     # wait 1 second
    led1.off()        # turn LED off
    print("LED 1 off")
    time.sleep(1)     # wait 1 second
    led2.on()         # turn LED on
    print("LED 2 on")
    time.sleep(1)     # wait 1 second
    led2.off()        # turn LED off
    print("LED 2 off")
    time.sleep(1)     # wait 1 second
    led3.on()         # turn LED on
    print("LED 3 on")
    time.sleep(1)     # wait 1 second
    led3.off()        # turn LED off
    print("LED 3 off")
    time.sleep(1)     # wait 1 second
