void setup() {
  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // Check if data is available to read from Python
  if (Serial.available() > 0) {
    // Read the data from Python
    String dataFromPython = Serial.readString();

    // Process the data as needed
    // For example, print it to the serial monitor
    Serial.println("Data from Python: " + dataFromPython);

    // Send a response back to Python if needed
    // For example, to acknowledge receipt of data
    Serial.println("Data received by Arduino");
  }
}