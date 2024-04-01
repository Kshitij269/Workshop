from pyfirmata import Arduino, util , OUTPUT
import time
import random

port = 'COM17'  # Change this to the appropriate port

# Create a new Arduino board instance
board = Arduino(port)

# Define the pins connected to the LEDs
led_pins = [2, 3, 4, 5, 6]

# Set the mode of each pin to OUTPUT
for pin in led_pins:
    board.digital[pin].mode = OUTPUT

# Sequential Blinking
def sequential_blink():
    while True:
        for pin in led_pins:
            board.digital[pin].write(1)  # Turn LED on
            time.sleep(0.5)
            board.digital[pin].write(0)  # Turn LED off

# Simultaneous Blinking
def simultaneous_blink():
    while True:
        for pin in led_pins:
            board.digital[pin].write(1)  # Turn all LEDs on
        time.sleep(0.5)
        for pin in led_pins:
            board.digital[pin].write(0)  # Turn all LEDs off
        time.sleep(0.5)

# Alternating Blinking
def alternating_blink():
    while True:
        for i in range(0, len(led_pins), 2):
            board.digital[led_pins[i]].write(1)  # Turn on LED at even index
            board.digital[led_pins[i+1]].write(1)  # Turn on LED at odd index
            time.sleep(0.5)
            board.digital[led_pins[i]].write(0)  # Turn off LED at even index
            board.digital[led_pins[i+1]].write(0)  # Turn off LED at odd index

# Knight Rider Effect
def knight_rider():
    while True:
        for i in range(len(led_pins)):
            board.digital[led_pins[i]].write(1)  # Turn on LED
            time.sleep(0.1)
            board.digital[led_pins[i]].write(0)  # Turn off LED
        for i in range(len(led_pins)-2, 0, -1):
            board.digital[led_pins[i]].write(1)  # Turn on LED
            time.sleep(0.1)
            board.digital[led_pins[i]].write(0)  # Turn off LED

# Random Blinking
def random_blink():
    while True:
        for pin in led_pins:
            board.digital[pin].write(random.randint(0, 1))  # Randomly turn LED on or off
        time.sleep(0.5)

# Execute the desired pattern
simultaneous_blink()  # Change this to any function name to execute a different pattern
