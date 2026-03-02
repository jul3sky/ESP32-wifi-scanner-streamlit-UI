# TWO OPPOSITE WAYS TO WIRE A BUTTON
=====================================================================================
A button can be wired in two valid ways:

1) Active‑low button (current setup)
- Uses internal pull‑up
- Pin is HIGH when not pressed
- Pressing the button connects the pin to GND
- Pressed = 0
This is the most common pattern on ESP32 and Arduino.

2) Active‑high button (my older code, like (https://github.com/jul3sky/morse-blinker))
- Uses pull‑down resistor (internal or external)
- Pin is LOW when not pressed
- Pressing the button connects the pin to 3.3V
- Pressed = 1
This is the opposite logic.

## WHY MY OLDER CODE GAVE 1 WHEN PRESSED
=====================================================================================
In that older code, i did the following:

- I used Pin.PULL_DOWN instead of Pin.PULL_UP

- The button was wired between GPIO → 3.3V, not GPIO → GND
  
- The example code I followed used active‑high logic
  
In that configuration:
- Not pressed → pin floats LOW → reads 0
- Pressed → pin gets 3.3V → reads 1
So the button logic flips depending on the wiring.

## WHY MY CURRENT CODE SHOWS "LOW" (0 = PRESSED)
=====================================================================================
The current line:
`button = Pin(16, Pin.IN, Pin.PULL_UP)`
forces the pin to be HIGH by default.

Pressing the button pulls it to GND → LOW → 0.
This is the standard ESP32 pattern because:
- pull‑ups are built‑in
- grounding a pin is safer
- less electrical noise
- fewer false triggers
That’s why most MicroPython examples use active‑low.

## HOW TO CHECK WHICH LOGIC A BUTTON USES
========================================================================================
Let's look at two things:
Wiring:
- GPIO → GND → active‑low
- GPIO → 3.3V → active‑high
Code:
- Pin.PULL_UP → active‑low
- Pin.PULL_DOWN → active‑high
Once those two are learned, the logic becomes predictable.

## A SIMPLE RULE TO REMEMBER
=========================================================================================
- PULL_UP → pressed = 0
- PULL_DOWN → pressed = 1
Everything else follows from that.

===============================================================================================================
# END OF THE FILE
===============================================================================================================
