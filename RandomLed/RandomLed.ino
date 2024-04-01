int ledPins[] = {2, 3, 4, 5, 6};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 5; j++) {
      digitalWrite(ledPins[j], HIGH);
      delay(50);
      digitalWrite(ledPins[j], LOW);
      delay(50);
    }
    delay(400); // Adjust delay to change the heartbeat rate
  }
  delay(1000); // Delay between heartbeats
}
