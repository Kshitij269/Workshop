int ledPins[] = {2, 3, 4, 5, 6}; // Array to hold the LED pins

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT); // Set each pin as an output
  }
}

void loop() {
  for (int i = 0; i < 5; i++) {
    digitalWrite(ledPins[i], HIGH); // Turn on the current LED
    delay(500); // Wait for 0.5 seconds
    digitalWrite(ledPins[i], LOW); // Turn off the current LED
    delay(500); // Wait for 0.5 seconds
  }
}
