from pyfirmata import Arduino, util
import time
from pyfirmata import Arduino , OUTPUT

# Define the port where the Arduino is connected
port = 'COM17'  # Change this to the appropriate port

# Create a new Arduino board instance
board = Arduino(port)

# Define the pins connected to the LEDs
led_pins = [2, 3, 4, 5, 6]

# Set the mode of each pin to OUTPUT
for pin in led_pins:
    board.digital[pin].mode = OUTPUT

# Wait for 1 second at every LED state change
wait = 1

# Initialize all LEDs to False (off)
led_states = [False] * len(led_pins)

# Iterate through all possible combinations of LED states
while True:
    for i in range(2 ** len(led_pins)):
        for j in range(len(led_pins)):
            board.digital[led_pins[j]].write(led_states[j])
        print([int(state) for state in led_states])
        
        # Update LED states for the next iteration
        for j in range(len(led_pins)):
            if (i >> j) & 1:
                led_states[j] = True
            else:
                led_states[j] = False
        
        time.sleep(wait)

# Clean up and exit
board.exit()
