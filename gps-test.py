import pigpio
import time

RX_PIN = 13
TX_PIN = 26

pi = pigpio.pi() 

pi.set_mode(RX_PIN, pigpio.INPUT);
pi.set_mode(TX_PIN, pigpio.OUTPUT);

def read_bit(pin):
    return pi.read(pin)

def write_bit(pin, value):
    pi.write(pin, value) 

try:
    while True:
        data = read_bit(RX_PIN)
        print(data)
        time.sleep(0.5)
        """
        write_bit(TX_PIN, 1)
        time.sleep(0.01)
        """
except KeyboardInterrupt:
    pi.stop()