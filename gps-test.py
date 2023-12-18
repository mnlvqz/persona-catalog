import time
import serial
import RPi.GPIO as GPIO

# Serial GPIO pins
TX_PIN = 26
RX_PIN = 13

# GPIO configuration
GPIO.setmode(GPIO.BCM)
GPIO.setup(TX_PIN, GPIO.OUT)
GPIO.setup(RX_PIN, GPIO.IN)

ser = serial.Serial(
    port='/dev/serial0',  
    baudrate=9600, 
)

def read_serial():
    while True:
        if GPIO.input(RX_PIN):
            line = ser.readline().decode('utf-8').rstrip()
            print(line)

try:
    read_serial()
except KeyboardInterrupt:
    GPIO.cleanup()