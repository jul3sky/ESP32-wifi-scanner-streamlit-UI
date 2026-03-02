from machine import Pin
import time

button = Pin(16, Pin.IN, Pin.PULL_UP) # see the schematics to choose the right pin

print("Press the button...")

while True:
    if button.value() == 0: 
        print("Button pressed!")
        time.sleep(0.2)
