"""ESP32 V3 MicroPython-based WIFI-Scanner firmware"""


# ---- IMPORT LIBRARIES ----
import network 
import binascii
import time
import json 
from machine import Pin



# ---- START BUTTON SETUP ----
start_button = Pin(4, Pin.IN, Pin.PULL_UP) 

# ---- STOP BUTTON SETUP ----
stop_button = Pin(0, Pin.IN, Pin.PULL_UP)

# ---- WIFI INITIATION ----
wlan = network.WLAN(network.WLAN.IF_STA) # enable station interface (network interface card)
wlan.active(True)

# ---- WAIT FOR START BUTTON ----
print("Press START button to begin scanning...")

while start_button.value() == 1:   # 1 = not pressed (pull-up)
    time.sleep(0.05)

print("Starting scanner!")


# ---- SCANNING FOR NETWORKS WITH JSON OUTPUT ----
while True: # scanning goes infinitely in loop

    # check stop button
    if stop_button.value() == 0:   # stop button pressed
        print("Scanner stopped.")
        break

    networks = wlan.scan() # perform scan

    for ssid, bssid, channel, rssi, authmode, hidden in networks:
        entry = {
            "ssid": ssid.decode(), 
            "rssi": rssi,
            "channel": channel,
            "bssid": binascii.hexlify(bssid).decode() # here we turn binary data into hex
        }
        print(json.dumps(entry)) # wifi endpoint paraneters dumps into JSON file

    time.sleep(2) 
