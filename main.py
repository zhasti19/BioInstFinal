import numpy as np
import matplotlib.pyplot as plt
import serial 
import time

# Establish serial connection with Arduino
arduino = serial.Serial('COM3', 9600)  # Adjust port and baud rate as needed

# Function to receive data from PowerLab
def receive_data_from_powerlab():
    # Sample implementation, replace with your actual code to receive data
    data_from_powerlab = b'SomeData'  # Sample data
    return data_from_powerlab

# Main loop
while True:
    # Receive data from PowerLab
    data = receive_data_from_powerlab()
    
    # Process data as needed
    processed_data = data  # Placeholder, replace with actual processing
    
    # Send data to Arduino
    arduino.write(processed_data)
    
    # Optional: Wait for response from Arduino
    response = arduino.readline()
    print("Response from Arduino:", response.decode().strip())
    
    # Optional: Delay between data transmissions
    time.sleep(1)

# # Sample data
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# # Create a plot
# plt.plot(x, y)

# # Add title and labels
# plt.title('Simple Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# # Add grid
# plt.grid(True)

# # Show plot
# plt.show()