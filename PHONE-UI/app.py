"UI application for Wifi Scanner"


import streamlit as st 
import serial
import json
from prettytable import PrettyTable



st.title("ESP32 WiFi Scanner") # name of the app

# ---- ON/OFF BUTTON ----






if "results" not in st.session_state:
    st.session_state.results = [] # list with scan results for each session

# ---- OPEN USB SERIAL PORT ----
ser = serial.Serial('/dev/ttyACM0', 115200) # you need to confirm the correct serial device path
                                            # it is NOT on ESP 32 


placeholder = st.empty()

# ---- READ FROM ESP32 / PARSE JSON ----
for _ in range(20):

    line = ser.readline().decode().strip()
    if line:
        try:
            data = json.loads(line)
            placeholder.write(data)
        except:
            pass

# ---- STREAMLIT TABLE FOR JSON SCAN RESULTS----
st.table(st.session_state.results)


# ---- UPDATE A TABLE IN REAL TIME USING PRETTY TABLE ----
if st.session_state.results:
    table = PrettyTable() # build PrettyTable

    headers = list(st.session_state.results[0].keys()) # use keys from the first JSON object as headers
    table.field_names = headers

    for row in st.session_state.results:
        table.add_row([row[h] for h in headers]) # add all rows

    st.text(table) # render PrettyTable inside Streamlit

# ---- AUTO REFRESH ----
time.sleep(0.2)
st.experimental_rerun()
