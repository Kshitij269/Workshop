#include <Servo.h>

Servo myservo;  // Create a servo object

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  // Attach servo to pin 9
  myservo.attach(10);
}

void loop() {
  // Check if data is available to read from serial port
  if (Serial.available() > 0) {
    // Read the slider value from serial
    int slider_value = Serial.parseInt();
    // Constrain slider value between 0 and 180
    slider_value = constrain(slider_value, 0, 180);
    // Set servo position based on slider value
    myservo.write(slider_value);
  }
}
