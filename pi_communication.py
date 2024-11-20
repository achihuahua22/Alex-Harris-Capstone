import serial

# Initialize Serial Port
ser = serial.Serial(port = 'dev/tty/AMA0', baud = 9600, parity= serial.PARITY_NONE,timeout=1)
