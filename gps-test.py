import pigpio
import time

RX_PIN = 13
TX_PIN = 26

pi = pigpio.pi() 

pi.set_mode(RX_PIN, pigpio.INPUT);
pi.set_mode(TX_PIN, pigpio.OUTPUT);
