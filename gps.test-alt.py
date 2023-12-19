
import serial
import time

uart = serial.Serial("/dev/tty50", 9600)
print("Loading...")
uart.flush()
while True:
    try:
        data = uart.readline().decode('utf-8')
        if(data[0:6] == "$GPGGA"):
            print(data)
            uart.flush()
    except:
        print(".")
        uart = serial.Serial("/dev/tty50", 9600)
