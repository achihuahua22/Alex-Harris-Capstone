#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <wiringPi.h>
#include <wiringSerial.h>
#include <wiringPiI2C.h>
#include <arpa/inet.h>

#define SERIAL_PORT "/dev/serial0" // GPIO UART on Raspberry Pi 4
#define I2C_ADDRESS 0x40           // I2C device address
#define SERVER_IP "192.168.1.100"  // Replace with your server IP
#define SERVER_PORT 8080           // Replace with your server port

int main() {
    int serial_fd, i2c_fd, sock_fd;
    struct sockaddr_in server_addr;
    char buffer[256];
    int bytes_read;

    // Initialize WiringPi
    if (wiringPiSetup() == -1) {
        perror("wiringPiSetup failed");
        return 1;
    }

    // Open serial port (GPIO UART)
    serial_fd = serialOpen(SERIAL_PORT, 9600);
    if (serial_fd < 0) {
        perror("Unable to open serial port");
        return 1;
    }

    // Initialize I2C
    i2c_fd = wiringPiI2CSetup(I2C_ADDRESS);
    if (i2c_fd < 0) {
        perror("Unable to initialize I2C");
        return 1;
    }

    // Create socket
    sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd < 0) {
        perror("Socket creation failed");
        return 1;
    }

    // Configure server address
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(SERVER_PORT);
    if (inet_pton(AF_INET, SERVER_IP, &server_addr.sin_addr) <= 0) {
        perror("Invalid address/Address not supported");
        return 1;
    }

    // Connect to server
    if (connect(sock_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Connection failed");
        return 1;
    }

    printf("Connected to server at %s:%d\n", SERVER_IP, SERVER_PORT);

    // Main loop
    while (1) {
        // Read from serial port (GPIO UART)
        bytes_read = read(serial_fd, buffer, sizeof(buffer) - 1);
        if (bytes_read > 0) {
            buffer[bytes_read] = '\0'; // Null-terminate the string
            printf("Serial data: %s\n", buffer);

            // Send serial data to server
            send(sock_fd, buffer, bytes_read, 0);
        }

        // Read from I2C device
        int i2c_data = wiringPiI2CRead(i2c_fd);
        if (i2c_data >= 0) {
            printf("I2C data: %d\n", i2c_data);

            // Send I2C data to server
            snprintf(buffer, sizeof(buffer), "I2C: %d\n", i2c_data);
            send(sock_fd, buffer, strlen(buffer), 0);
        }

        // Sleep for a short time
        usleep(100000); // 100ms
    }

    // Cleanup (not reached in this example)
    serialClose(serial_fd);
    close(sock_fd);
    return 0;
}