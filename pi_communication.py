import serial
import roslibpy
# Initialize Serial Port
ser = serial.Serial(port = 'dev/tty/AMA0', baud = 9600, parity= serial.PARITY_NONE,timeout=1)

# Repeatedly print serial line.
while 1:
    x = ser.readline()
    print(x)