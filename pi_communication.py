#!/usr/bin/env python
import serial
import smbus2
import rospy
import time
from smbus2 import SMBus
from std_msgs.msg import String

#import roslibpy
# Initialize Serial Port
#ser = serial.Serial(port = 'dev/ttyAMA0', baud = 9600, parity= serial.PARITY_NONE,timeout=1)

# # create a smbus object
# bus = smbus2.SMBus(1)
# time.sleep(1)
# b = bus.read_byte_data(80,0)

# #look at spi adapter documentation to see address information
# #might need to move one of the dip switches.

# # Repeatedly print spi byte data.
# while 1:
#     print(b)


# #need to turn the two inputs in the spi bus into two distinct publisher nodes, then done i think :)
# client = rospy.Ros(host='localhost', port=9090)


def talker():
    rospy.init_node("test_node")
    rospy.loginfo("hello")
    # pub = rospy.Publisher('chatter', String, queue_size=10)
    # rospy.init_node('talker', anonymous=True)
    # rate = rospy.Rate(10) # 10hz
    # while not rospy.is_shutdown():
    #     hello_str = "hello world %s" % rospy.get_time()
    #     rospy.loginfo(hello_str)
    #     pub.publish(hello_str)
    #     rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
           pass