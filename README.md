# ESP32 WiFi Scanner — MicroPython + Streamlit Dashboard
A complete beginner‑friendly and educational project for learning embedded systems, serial communication, and real‑time dashboards.


Overview
This project turns an ESP32 into a live WiFi scanner that streams network information (SSID, RSSI, channel, BSSID) as JSON over USB.
A Streamlit application running on a phone or computer reads this JSON stream and displays it in a live‑updating dashboard.
The goal is not only to build a working tool, but also to teach:
- how microcontrollers communicate over USB
- how to structure JSON data on embedded devices
- how to build a reactive UI with Streamlit
- how to integrate hardware + firmware + software into one system
This repository is intentionally written for learners. Every step is explained.

Project Architecture
┌──────────────────────────────┐
│          ESP32               │
│  MicroPython Firmware         │
│  - Scans WiFi networks        │
│  - Formats results as JSON    │
│  - Streams JSON over USB      │
└──────────────┬───────────────┘
               │ USB‑CDC Serial
               ▼
┌──────────────────────────────┐
│        Streamlit App         │
│  - Reads serial JSON stream  │
│  - Parses JSON               │
│  - Displays live table       │
│  - PrettyTable + Streamlit   │
└──────────────────────────────┘


The ESP32 acts as a sensor.
The Streamlit app acts as a dashboard.

ESP32 Firmware (MicroPython)
What the firmware does
- Initializes the WiFi interface in station mode
- Scans for nearby networks
- Extracts:
- SSID
- RSSI (signal strength)
- Channel
- BSSID (MAC address)
- Converts each scan result into a JSON object
- Prints JSON lines over USB
- Repeats every 2 seconds
- Stops when a physical button is pressed
Why JSON?
JSON is:
- human‑readable
- easy to parse in Python
- perfect for streaming line‑by‑line
- widely used in IoT dashboards


📱 Streamlit Dashboard
What the UI does
- Opens the USB serial port
- Reads JSON lines from the ESP32
- Parses each line into a Python dictionary
- Stores results in st.session_state
- Displays:
- a Streamlit table
- a PrettyTable ASCII table
- Auto‑refreshes every 0.2 seconds
Why Streamlit?
- Easy to build dashboards
- Auto‑refreshing UI
- Works on Android (Termux/Pydroid)
- Perfect for real‑time data



Connecting ESP32 to Your Phone or PC
On Windows/macOS/Linux
The ESP32 usually appears as:
- /dev/ttyACM0
- /dev/ttyUSB0
- COM3, COM4, etc.
On Android (Termux or Pydroid)
The device path may vary:
- /dev/ttyACM0
- /dev/ttyUSB0
- Or via Termux USB API
You may need to adjust the serial port path in app.py.

How to Run the Project
1. Flash MicroPython to ESP32
Use esptool.py or the official flasher.
2. Upload main.py to ESP32
Using:
- Thonny
- ampy
- rshell
- mpremote
3. Connect ESP32 to your phone or PC
Use a USB‑C cable.
4. Install dependencies on your phone/PC
pip install streamlit prettytable pyserial


5. Run the Streamlit app
streamlit run app.py


6. Watch the dashboard update in real time
Every 0.2 seconds, new scan results appear.

Educational Concepts Covered
This project teaches:
Embedded Systems
- MicroPython runtime
- WiFi scanning
- GPIO input
- JSON serialization
Serial Communication
- USB‑CDC
- Line‑based streaming
- Non‑blocking reads
Data Engineering
- JSON parsing
- Session state management
- Real‑time data pipelines
UI Development
- Streamlit reactive model
- PrettyTable formatting
- Auto‑refreshing dashboards
System Integration
- Hardware + firmware + software
- Cross‑platform communication
- Real‑time visualization
This is the same architecture used in professional IoT dashboards.

Why This Project Is Advanced (Even If It Doesn’t Feel Like It)
You are combining:
- microcontroller firmware
- serial protocol design
- JSON data modeling
- real‑time UI rendering
- cross‑platform integration
Most beginners never attempt this.
Many university courses don’t cover this level of integration.
This project is equivalent to a junior IoT engineer’s prototype or a university capstone project.


