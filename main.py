import numpy as np
import matplotlib.pyplot as plt
import serial 
import time
from matplotlib.animation import FuncAnimation

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

# Parameters
sampling_rate = 1000  # Hz
duration = 5  # seconds
N = sampling_rate * duration  # Number of samples
t = np.linspace(0, duration, N)
frequency = 50  # Hz
amplitude = 2

# Create a figure and axis for the plot
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Magnitude')
ax.set_title('Real-time FFT Magnitude Spectrum')
ax.grid(True)

# Initialize empty arrays for storing data
signal = np.zeros(N)
frequencies = np.fft.fftfreq(N, 1 / sampling_rate)
fft_result = np.zeros(N)

# Function to generate new data for the plot
def update(frame):
    global signal, fft_result

    # Generate new sample data (replace this with your real-time data acquisition)
    signal[:-1] = signal[1:]
    signal[-1] = amplitude * np.sin(2 * np.pi * frequency * t[-1])

    # Compute the FFT
    fft_result = np.fft.fft(signal)

    # Update the plot
    line.set_data(frequencies, np.abs(fft_result))
    ax.relim()
    ax.autoscale_view(True, True, True)

    return line,

# Animate the plot
ani = FuncAnimation(fig, update, blit=True, interval=50)

plt.show()