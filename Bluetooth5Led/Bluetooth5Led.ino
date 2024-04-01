#include <SoftwareSerial.h>

// Define LED pins
const int ledPins[] = {2, 3, 4, 5, 6};
const int numLEDs = sizeof(ledPins) / sizeof(ledPins[0]);

// Initialize LED states
bool ledStates[numLEDs] = {LOW};

// Define Bluetooth module's RX and TX pins
const int bluetoothRxPin = 10;
const int bluetoothTxPin = 11;

// Create a SoftwareSerial object for Bluetooth communication
SoftwareSerial bluetooth(bluetoothRxPin, bluetoothTxPin);

void setup() {
  // Initialize serial communication with Bluetooth module
  Serial.begin(9600);
  bluetooth.begin(9600);
  
  // Set LED pins as outputs
  for (int i = 0; i < numLEDs; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  // Check if data is available to read from Bluetooth module
  if (bluetooth.available() > 0) {
    char command = bluetooth.read();
  
    Serial.print(command);
    // If command is a digit between 1 and numLEDs, toggle corresponding LED
    if (command >= '1' && command <= ('0' + numLEDs)) {
      int ledIndex = command - '1';
      ledStates[ledIndex] = !ledStates[ledIndex];
      digitalWrite(ledPins[ledIndex], ledStates[ledIndex]);
    }
    else if (command == '6'){
      for (int i=0;i<5;i++){
        digitalWrite(ledPins[i], HIGH);
        ledStates[i] = HIGH;
      
      }
    }
    else if (command == '7'){
       for (int i=0;i<5;i++){
        digitalWrite(ledPins[i], LOW);
        ledStates[i] = LOW;

      }
    }
  }
}
