
"""
Client Script for Xbox Controller over Bluetooth
-------------------------------------------------

Description:
This script reads Xbox controller inputs over Bluetooth and sends the data
to the Raspberry Pi over Ethernet using socket communication.

Prerequisite:
Ensure that the Xbox controller is paired with the laptop via Bluetooth before running this script.
"""

import pygame
import socket
import json

# Initialize pygame and Xbox controller
pygame.init()
pygame.joystick.init()

try:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Controller {joystick.get_name()} initialized.")
except pygame.error:
    print("No controller found. Ensure the Xbox controller is paired via Bluetooth.")
    exit()

# Set up the socket connection to Raspberry Pi
raspberry_pi_ip = '192.168.1.3'  # Replace with Raspberry Pi's IP
port = 8080
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((raspberry_pi_ip, port))
print("Connected to Raspberry Pi.")

try:
    while True:
        pygame.event.pump()

        # Capture joystick axes and button states
        axes = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
        buttons = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]

        # Create a JSON payload with the data
        data = {'axes': axes, 'buttons': buttons}

        # Send the data to Raspberry Pi
        client_socket.send(json.dumps(data).encode('utf-8'))

except KeyboardInterrupt:
    print("Exiting...")
finally:
    client_socket.close()
    print("Socket closed.")
