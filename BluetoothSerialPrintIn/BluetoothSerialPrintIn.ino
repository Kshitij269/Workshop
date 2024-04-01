#include <SoftwareSerial.h>

// Define the analog pin for the sensor
const int sensorPin = A0;

// Define Bluetooth module's RX and TX pins
const int bluetoothRxPin = 10;
const int bluetoothTxPin = 11;

// Create a SoftwareSerial object for Bluetooth communication
SoftwareSerial bluetooth(bluetoothRxPin, bluetoothTxPin);

void setup() {
  // Initialize serial communication with Bluetooth module
  Serial.begin(9600);
  bluetooth.begin(9600);
}

void loop() {
  // Read sensor value
  int sensorValue = analogRead(sensorPin);

  // Send sensor value over Bluetooth
  bluetooth.print(sensorValue);
  bluetooth.print('\n'); // Add a newline character to indicate end of message

  // Delay before next reading
  delay(1000); // Adjust as needed
}
