import pigpio
import time

TX_PIN = 26
RX_PIN = 13

pi = pigpio.pi()

serial_port = pi.serial_open("/dev/ttyS0", 9600, rxpin=RX_PIN, txpin=TX_PIN)

try:
    while True:
        if pi.serial_data_available(serial_port):
            # Leer una línea de datos
            line = pi.serial_readline(serial_port).decode('utf-8').rstrip()
            print(line)
        time.sleep(0.1)
except KeyboardInterrupt:
    pi.serial_close(serial_port)  # Cerrar el puerto serial
    pi.stop()