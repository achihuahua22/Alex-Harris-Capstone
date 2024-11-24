import serial
import roslibpy
from smbus2 import SMBus

# create a smbus object
bus = SMBus(1)
b = bus.read_byte_data(80,0)

#look at spi adapter documentation to see address information
#might need to move one of the dip switches.

# Repeatedly print spi byte data.
while 1:
    print(b)


#need to turn the two inputs in the spi bus into two distinct publisher nodes, then done i think :)
client = roslibpy.Ros(host='localhost', port=9090)