import serial
<<<<<<< HEAD
import roslibpy
from smbus2 import SMBus
=======
#import roslibpy
# Initialize Serial Port
ser = serial.Serial(port = 'dev/tty/AMA0', baud = 9600, parity= serial.PARITY_NONE,timeout=1)
>>>>>>> 5b63914d6b97058a6b6de2c9be6284c41ff6858b

# create a smbus object
bus = SMBus(1)
b = bus.read_byte_data(80,0)

#look at spi adapter documentation to see address information
#might need to move one of the dip switches.

# Repeatedly print spi byte data.
while 1:
<<<<<<< HEAD
    print(b)


#need to turn the two inputs in the spi bus into two distinct publisher nodes, then done i think :)
client = roslibpy.Ros(host='localhost', port=9090)
=======
    #x = ser.readline()
    print("test")
>>>>>>> 5b63914d6b97058a6b6de2c9be6284c41ff6858b
