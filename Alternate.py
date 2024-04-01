from pyfirmata import Arduino
from time import sleep

# Connecting to the board
board = Arduino('COM17')

# Initializing the LEDs
led1 = board.get_pin('d:2:o')
led2 = board.get_pin('d:3:o')
led3 = board.get_pin('d:4:o')
led4 = board.get_pin('d:5:o')
led5 = board.get_pin('d:6:o')

# Wait for 1s at every count value
wait = 1

# Initialize all LEDs to False (off)
val_1 = val_2 = val_3 = val_4 = val_5 = False

# led5 is the least significant bit and led1 is the most significant bit
while True:  # This is an infinite loop which won't end until the terminal is killed
    for _ in range(2):
        for _ in range(2):
            for _ in range(2):
                for _ in range(2):
                    for _ in range(2):
                        sleep(wait)
                        # Updating the values and printing them
                        led1.write(val_1)
                        led2.write(val_2)
                        led3.write(val_3)
                        led4.write(val_4)
                        led5.write(val_5)
                        print(int(val_1), int(val_2), int(val_3), int(val_4), int(val_5))

                        val_5 = not val_5
                    val_4 = not val_4
                val_3 = not val_3
            val_2 = not val_2
        val_1 = not val_1
    print("\n\n")
