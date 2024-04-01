import tkinter as tk
import serial

serial_port = 'COM21'  # Change this to match the serial port of your Arduino
baud_rate = 9600

ser = serial.Serial(serial_port, baud_rate, timeout=1)

def update_servo_position(event):
    slider_value = slider.get()
    ser.write(bytes(str(slider_value), 'utf-8'))

window = tk.Tk()
window.title("Servo Control")

slider = tk.Scale(window, from_=0, to=180, orient=tk.HORIZONTAL, length=300)
slider.set(90)  # Set initial position to 90 degrees
slider.pack()


slider.bind("<ButtonRelease-1>", update_servo_position)

window.mainloop()
