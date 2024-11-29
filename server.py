
"""
Server Script for Xbox Controller Input
---------------------------------------

Description:
This script runs on the Raspberry Pi and listens for Xbox controller inputs
sent from a laptop over Ethernet. The received data includes joystick axes 
values and button states.

"""

import socket
import json

# Set up the server to listen for incoming data
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.1.3', 8080))  # Replace with Raspberry Pi's IP
server_socket.listen(1)
print("Waiting for a connection...")

conn, addr = server_socket.accept()
print(f"Connection from {addr} established.")

try:
    while True:
        # Receive data
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break

        # Parse the received JSON data
        controller_input = json.loads(data)
        axes = controller_input['axes']
        buttons = controller_input['buttons']

        # Print or process the controller inputs
        print(f"Axes: {axes}")
        print(f"Buttons: {buttons}")

except KeyboardInterrupt:
    print("Exiting...")
finally:
    conn.close()
    server_socket.close()
    print("Socket closed.")
