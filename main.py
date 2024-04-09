import numpy as np
import matplotlib.pyplot as plt
import serial 
import time
from matplotlib.animation import FuncAnimation
from PyNeuro.PyNeuro import PyNeuro

# Establish serial connection with Arduino
arduino = serial.Serial('COM3', 9600)  # Adjust port and baud rate as needed

# Initialize empty lists for storing data
attention = []
meditation = []

pn = PyNeuro()
pn.start()

while True:
    if pn.attention > 70: # Access data through object
        attention.append(1)
        pn.close()
    elif pn.attention < 40:
        attention.append(-1)
        pn.close()
    else:
        attention.append(0) 
        pn.close()
    if pn.meditation > 70:
        meditation.append(1)
        pn.close()
    elif pn.meditation < 40:
        meditation.append(-1)
        pn.close()
    else:
        meditation.append(0) 
        pn.close() 
    time.sleep(0.2)

    # Send data to Arduino
    arduino.write(attention)

    # Optional: Delay between data transmissions
    time.sleep(1)