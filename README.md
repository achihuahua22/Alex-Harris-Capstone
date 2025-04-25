# Alex Harris Capstone: Low Cost Device for Laboratory Equipment Integration
 _This project is a Raspberry Pi Hat that is intended to receive inputs from Self-Driving-Laboratory equipment and utilize the raspberry pi to publish device data onto the network.
This repository contains all of the schematics, documentation, and code necessary to build this device._

This project builds on an-ven’s [graspib](https://github.com/an-ven/graspib) project by adding more RS232 support and a UART breakout pin. 

It also utilizes the [Linux GPIB package](https://linux-gpib.sourceforge.io)

Currently, this device supports UART, RS232, and GPIB. 

![3d model of pcb](https://github.com/achihuahua22/Alex-Harris-Capstone/blob/main/capstone_rev4_3d_screenshot.png)

If you want to make one yourself, the files are [here](capstone_cad_rev4)



## Introduction
This project is a Raspberry Pi Hat that is intended to 
improve self driving lab connectivity and modularity 
by allowing researchers to integrate multiple lab 
devices into their networks. I worked with Dr. Taylor 
Sparks' self-driving laboratory (SDL) to develop a 
device to more easily network with lab equipment. 
A self-driving laboratory is a laboratory where
everything from specimen handling, experiments, 
and decision making is fully automated to 
accelerate research [1]. This device intends to be an 
easy-to-use device for networking and save 
researchers money. To make a device “easy to use” I 
wanted to work with hardware that researchers are 
familiar with. This led to me choosing to design a 
board that attaches to a Raspberry Pi. 
I chose to use a Raspberry Pi based solution
because of its prevalence in the research space. 
Many pieces of university research level lab 
equipment have very little interconnection due to 
the age of the device or the type of communication 
protocol. Another issue is that products can use 
proprietary connection methods, which makes the 
task of developing an interconnected SDL very 
difficult [2]. I wanted to develop a device that can 
put data collected by lab equipment onto the 
network using a Raspberry Pi and a circuit board 
that sits on top of the Pi to handle the 
communications.

## Design
### Methods
I began with researching similar solutions to this 
problem, and the two options were a series of adapter 
dongles, or a device that interfaces with a single board 
computer to allow for communication. I chose this 
method as it would be easiest for the end user to have a 
single device that handles lab equipment connectivity.
I started by purchasing pre-built adapter components 
and build a breadboard analog of the final device. This 
device consisted of RS232 adapters and a serial 
expansion board for a Raspberry Pi. With this, I was able 
to test the idea of sending device data over the network 
using ROS and the python socket library.

### Results
I designed a circuit board that could serve as an add on 
that connected to the Raspberry Pi’s GPIO port. To 
expand the capability of the device, a GPIB connection
was added, taking advantage of the open-source Linux 
GPIB package [3]. GPIB is a very common protocol with 
adapters often costing hundreds of dollars.
The board was manufactured by JLCPCB, hand 
assembled, revised, and tested thoroughly. A GitHub 
repository was maintained throughout the project 
detailing hardware and software setup instructions.
The low-cost goal was achieved with the total cost being 
around $40 for the entire device excluding shipping

### Conclusions
Improvements of the Linux GPIB library are needed to 
facilitate easy setup of hardware and improved 
compatibility with the IEEE-488 standard.
Future works should expand on the software for using 
the Raspberry Pi to communicate over the local 
network. Possibly a user interface to improve ease of 
use
Future works should also investigate more permanent, 
universal communication protocols to improve 
laboratory equipment integration.

### Communication Protocols
While there are many communication protocols used in laboratory equipment, a few come up most often when looking at the back of devices in labs around my university. Some of these include:

1. RS232
2. CAN (CAN-FD, etc.)
3. GPIB
4. USB
5. UART
6. HPIB
7. Ethernet

Obviously, it is not possible to develop a device to encompass every existing communication protocol, so I chose three that were most necessary to our SDL and were most feasible with the constraint of a Raspberry Pi powered device. The three protocols I chose were RS232, UART, and GPIB. I chose each of these for the following reasons:
#### _UART_
I chose UART because of its prevalence in open-source projects such as the OpenTrickler, a powder dispensing device that we are using in our SDL. UART is also a simple protocol to implement as it only requires four pins: 3v3, TX, RX, and GND. The end user can configure the Baud rate, parity or stop bits in software. I believe that including this communication allows for other SDLs to integrate their own custom devices and not have to design for network capabilities if they choose to use my device. 
#### _RS232_
I chose RS232 because it was very prevalent in older equipment in our lab such as the Fischer Scientific Analytical Scale, and some open-source devices such as the OpenRAMAN, a laser spectroscopy device for materials classification. While RS232 is an old communication protocol, it is still useful for simple communication of commands. 
#### _GPIB_
Lastly, I chose GPIB because it was also extremely prevalent in many types of laboratory equipment such as multimeters, spectrum analyzers, and other devices. The issue that many laboratories face with GPIB enabled devices is that adapters such as GPIB to USB can cost more than $1,000 and can only communicate with proprietary software. This can render perfectly usable lab equipment almost completely useless in terms of automation or remote data collection.

The following are protocols I didn't choose, future works could consider adding them.

#### _CAN_
I didn’t choose CAN or any of its variants (CAN, CAN-FD, CAN-XL) because it has too many variants to effectively develop a multipurpose product that could encompass of CAN. The differential pair nature of CAN also makes it difficult to develop for.
#### _USB_
I didn’t choose USB because of its complication with drivers, enumeration, host/peripheral, and all the headaches that come with that. In addition to this, a Raspberry Pi does not have the same driver setup as a normal computer which makes implementation difficult when this problem can be solved with a computer and a USB hub.
#### _HPIB_
I didn’t choose HPIB because of the general nature of GPIB (General Purpose Interface Bus) and how HPIB is limited to Hewlett-Packard devices, and that does not make sense with the intent of this project.
#### _Ethernet_
I didn’t choose Ethernet because it also defeats the purpose of this project. The Raspberry Pi used for this project has Ethernet connection capabilities, allowing me to develop a device that just handles the communications between the laboratory equipment and the Pi, reducing cost and complexity.


## Device Assembly
### PCB Manufacturing
At the time of writing, JLCPCB is a very good option for low cost PCB manufacturing. You can get 5 boards for roughly $4 not including shipping. All you need to do is zip these [Gerber Files](https://github.com/achihuahua22/Alex-Harris-Capstone/tree/main/capstone_rev4_gerbers), go to JLCPCB.com, click "upload gerbers" and choose the zipped file. Everything else should populate automatically. You don't need to do any configuration besides choosing the "Lead Free HASL" for a lead free surface finish on the pcb. Feel free to order a stencil as it might make surface mount soldering easier, not required though.

### Parts
Here is the [BOM](https://github.com/achihuahua22/Alex-Harris-Capstone/blob/main/bill_of_materials/senior_capstone_bom_rev4.csv) for the pcb components
   - Unfortunately, all of the components except for item 15 (SN75161BDW) can be purchased from Digikey, the remaining component can be purchased from Mouser
   - In addition, I would recommend M2.5 standoffs to support the board on top of the raspberry pi
   - Solder paste and Heat Gun is recommended for the Surface Mount components as the Resistors, Capacitors, and LED's

### Building
I would recommend using solder paste and a heat gun for installing the small surface mount components such as the resistors, capacitors, crystal and LED's and installing the components in the following order:
1. Resistors (R1-R12)
2. Crystal Oscillator (Y1)
3. Capacitors (C1-C8)
4. LED's (D1-D7) (*pay attention to the orientation of the LED!*)
   - The open part of the rectangle is the anode, the closed part is the cathode
5. Integrated Circuits (U1-U4) (In order of 1 to 4 is easiest)
6. Connectors

It is not required to install the components in this order, but is is easier to install the smaller components first so you don't have to navigate around the large connectors or IC's.
   
## Setup
1. Setup fresh install of [raspberry pi os](https://www.raspberrypi.com/software/)
2. Configure your network, password, etc to your liking
3. Download Provided [files](https://github.com/achihuahua22/Alex-Harris-Capstone/blob/main/send_to_network.c) to send data to network
4. From [graspib documentation](https://github.com/an-ven/graspib/tree/main) : 

   Install build tools and dependencies
   - Build tools: ```$ sudo apt install build-essential autoconf automake libtool flex bison```
   - RPi kernel headers: ```$ sudo apt install raspberrypi-kernel-headers```
   - Python3 headers: ```$ sudo apt install python3-dev```

    Download linux-gpib source files
   - Get release archives (4.3.4 or later) from https://sourceforge.net/projects/linux-gpib/files
   - or get the latest source from https://sourceforge.net/p/linux-gpib/code/HEAD/tree/

   Build and install kernel drivers
   - Enter linux-gpib-kernel directory ```$ cd linux-gpib-src-dir/linux-gpib-kernel```
   - Build kernel module by running make ```$ make```
   - Install kernel module ```$ sudo make install```
   - Update kernel module list ```$ sudo depmod -a```
   - Load gpib_bitbang kernel module ```$ sudo modprobe gpib_bitbang```
   - Now there should be some gpib* devices in /dev
   - Make the module loads on boot by adding gpib_bitbang line to /etc/modules-load.d/modules.conf

   When Raspberry Pi OS kernel gets upgraded, linux-gpib kernel module also needs to be rebuilt and reinstalled. 
   Basically just repeat above make and make install steps when kernel gets upgraded

   Build and install user space tools
   - Enter linux-gpib-user directory: ```$ cd linux-gpib-src-dir/linux-gpib-user```
   - If building from svn checkout first run bootstrap script: $ ./bootstrap
   - Run configure script: ```$ ./configure (run $ ./configure --help to list additional options)```
   - Build user space tools by running make: $ make
   - Install user space tools: ```$ sudo make install```
   - Make sure that shared library directory (default: /usr/local/lib/) is listed in: /etc/ld.so.conf.d/
   - Then run: $ sudo ldconfig

   Configure GPIB interface
   - Open gpib.conf configuration file $ sudo nano /usr/local/etc/gpib.conf (default location)
   - Set board_type = "gpib_bitbang" and other relevant settings (for details refer to included gpib.conf file, linux-gpib documentetion and included template file linux-gpib-src-dir/linux-gpib-user/util/template/gpib.conf)
   - Run gpib_config so the driver reads the configuration file $ sudo gpib_config --minor 0
   - Make the last command execute on every startup using crontab entry:
   - Edit crontab for root user: ```$ sudo crontab -e```
   - Add line the following line to cron tab file: @reboot /usr/local/sbin/gpib_config --minor 0
   - Enable non root users to use GPIB interface without sudo
   - Add new gpib system group: ```$ sudo groupadd -r gpib```
   - Append your_user_name to gpib supplementary group: ```$ sudo usermod -a -G gpib your_user_name```
   - Create /etc/udev/rules.d/99-gpib.rules file and add line: SUBSYSTEM=="gpib_common", GROUP="gpib", MODE="0660"

Reboot system to apply changes (udevadm utility can also be used, but reboot is dead simple to remember)
Test by running ibtest without sudo

5. Run and do the following to enable the I2C interface:
   - Open a terminal and run ```sudo raspi-config```
   - Select "Interface Options"
   - Select "P5 I2C"
   - It will prompt you with "Would you like the ARM I2C interface to be enabled?" *select yes*
   - Then it will prompt you to reboot *select yes*
   - After reboot, open another terminal and run ```sudo apt-get update``` and ```sudo apt-get install -y python3-smbus i2c-tools```
   - Finally shut down the raspberry pi with ```sudo halt```
   - Wait 10 seconds unplug power and restart
6. Run the following in the raspberry pi os terminal to configure serial and socket:
   
   - Update package list ```sudo apt update```
   - Install socket ```python3 -m pip install socket```
   - Install pySerial ```python3 -m pip install pyserial```
   - Install WiringPi ```sudo apt install wiringpi```
   - Install build tools ```sudo apt install build-essential```

7. See following [instructions](https://github.com/an-ven/graspib/tree/main) from grasPIB repository to configure the raspberry pi for GPIB
8. Configure Baud rate, IP, and I2C addresses in code




