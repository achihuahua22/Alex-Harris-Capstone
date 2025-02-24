# Alex-Harris-Capstone
### This project is a Raspberry Pi Hat that intends to receive inputs from Self-Driving-Laboratory equipment and automatically publish device data onto the network.
This repository contains all of the schematics, documentation, and code necessary to build this device.

Currently, this device supports UART, RS232, and GPIB*. 


## Introduction
For my senior capstone project, I worked with Dr. Taylor Spark’s self-driving laboratory (SDL) to develop a device to more easily integrate laboratory equipment into an SDL. This device intends to do two things: Allow researchers to easily put information about lab equipment onto their network and save them money. To make a device “easy to use” I wanted to work with hardware that researchers are familiar with as much as possible. This led to me choosing to design a product that is attached to a single board computer such as a Raspberry Pi. Using the Raspberry Pi was the obvious choice because of its prevalence in the research space. 
What do I mean by “integrating laboratory equipment”? A lot of laboratory equipment at a university research level has very little connection between devices either due to the age of the device or the type of communication protocol included. Another issue is that products can use proprietary connection methods, such as costly software or connectors. This makes the task of developing an interconnected SDL very difficult, especially when you are a student or researcher, or hobbyist with limited resources. 
I want to develop a device that can put data collected by lab equipment onto the network using a Raspberry Pi and HAT, or a PCB that sits on top of the Pi to handle the communications. The Pi will have an ethernet connection to the network, allowing the user to program it to either send data to a network address or something like a ROS network.
Methods
### Communication Protocols
While there are many communication protocols used in laboratory equipment, a few come up most often when looking at the back of devices in labs around my university. Some of these include:
•	RS232
•	CAN (CAN-FD, etc.)
•	GPIB
•	USB
•	UART
•	HPIB
•	Ethernet

Obviously, it is not possible to develop a device to encompass every existing communication protocol, so I chose three that were most necessary to our SDL and were most feasible with the constraint of a Raspberry Pi powered device. The three protocols I chose were RS232, UART, and GPIB. I chose each of these for the following reasons:
#### UART
I chose UART because of its prevalence in open-source projects such as the OpenTrickler, a powder dispensing device that we are using in our SDL. UART is also a simple protocol to implement as it only requires four pins: 3v3, TX, RX, and GND. The end user can configure the Baud rate, parity or stop bits in software. I believe that including this communication allows for other SDLs to integrate their own custom devices and not have to design for network capabilities if they choose to use my device. 
#### RS232
I chose RS232 because it was very prevalent in older equipment such as the Fischer Scientific Analytical Scale, and some open-source devices such as the OpenRAMAN, a laser spectroscopy device for materials classification. While RS232 is an old communication protocol, it is still useful for simple communication of commands. 
#### GPIB
Lastly, I chose GPIB because it was also extremely prevalent in many types of laboratory equipment such as multimeters, spectrum analyzers, and other devices. The issue that many laboratories face with GPIB enabled devices is that adapters such as GPIB to USB can cost more than $1,000 and can only communicate with proprietary software. This can render perfectly usable lab equipment almost completely useless in terms of automation or remote data collection.

I also want to discuss the protocols I didn’t choose.

#### CAN
I didn’t choose CAN or any of its variants (CAN, CAN-FD, CAN-XL) because it has too many variants to effectively develop a multipurpose product that could encompass of CAN. The differential pair nature of CAN also makes it difficult to develop for.
#### USB
I didn’t choose USB because of its complication with drivers, enumeration, host/peripheral, and all the headaches that come with that. In addition to this, a Raspberry Pi does not have the same driver setup as a normal computer which makes implementation difficult when this problem can be solved with a computer and a USB hub.
#### HPIB
I didn’t choose HPIB because of the general nature of GPIB (General Purpose Interface Bus) HPIB is limited to Hewlett-Packard devices, and that does not make sense with the intent of this project.
#### Ethernet
I didn’t choose Ethernet because it also defeats the purpose of this project. The Raspberry Pi used for this project has Ethernet connection capabilities, allowing me to develop a device that just handles the communications between the laboratory equipment and the Pi, reducing cost and complexity.
