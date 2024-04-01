from pyfirmata import Arduino, util
import time

port = 'COM17'
board = Arduino(port)

analog_pin = board.get_pin('a:0:i')
led_pin = board.get_pin('d:13:o')
it = util.Iterator(board)
it.start()

while True:
    analog_value = analog_pin.read()
    print(analog_value)
    if analog_value is not None and analog_value > 0.75:
        led_pin.write(1)
    else:
        led_pin.write(0)
    time.sleep(0.1)
