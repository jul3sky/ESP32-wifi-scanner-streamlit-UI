# HOMEMADE BUTTON PROTOTYPE
## (Aluminium Thread + Hair Ties)
============================================================================================
This project originally started before the hardware kit arrived, so a temporary button was built using:
- aluminium thread
- latex mini hair ties
- ESP32 header pins
- cardboard as a work surface
  
Despite being improvised, the button worked reliably enough to trigger GPIO input events.

**How it works**
--------------------------------------------------------------------------------------
A button is simply two conductors that touch when pressed. The prototype used:
- one aluminium thread attached to GPIO 16 pin
- one aluminium thread attached to GND
- pressing them together pulled the GPIO pin LOW
The ESP32 internal pull‑up resistor kept the pin HIGH when not pressed.
(Later on I created on Off button in the same way using GPIO 3 pin and GND)

![board schematics](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/08/ESP32-DOIT-DEVKIT-V1-Board-Pinout-30-GPIOs-Copy.png?quality=100&strip=all&ssl=1)
<sub>Schematics of ESP32</sub>

**Photos**
----------------------------------------------------------------------------------------
![Start of the project](https://github.com/jul3sky/ESP32-wifi-scanner-streamlit-UI/blob/main/homemade_button/assets/1772317847274.jpg)
<sub>Preparation for work</sub>

![Pin attachment](https://github.com/jul3sky/ESP32-wifi-scanner-streamlit-UI/blob/main/homemade_button/assets/1772317850671.jpg)
<sub>Pins are attached</sub>

![Button test](https://github.com/jul3sky/ESP32-wifi-scanner-streamlit-UI/blob/main/homemade_button/assets/1772317848012.jpg)
<sub>Since there are names of the real wi-fi endpoints shown in scan results, i cropped them out</sub>

----------------------------------------------------------------------------------------
**Why this matters**
----------------------------------------------------------------------------------------
This prototype demonstrates:
- resourceful engineering
- understanding of GPIO logic
- ability to test software before proper hardware arrives
It also shows the early evolution of the project.

=======================================================================================
# END OF FILE
=======================================================================================
