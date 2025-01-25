from cryptography.fernet import Fernet
import os

def decrypt_file(file_path, fernet):
    # Open the file and read its encrypted data
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    
    try:
        # Decrypt the data using the provided key
        decrypted_data = fernet.decrypt(encrypted_data)
        
        # Write the decrypted data back to the file (in plaintext)
        with open(file_path, "wb") as file:
            file.write(decrypted_data)
        print(f"Decrypted: {file_path}")
    
    except Exception as e:
        print(f"Error decrypting file {file_path}: {e}")

def decrypt_folder(folder_path, fernet):
    # Walk through the folder and decrypt any .txt files
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):  # Decrypt only .txt files
                file_path = os.path.join(root, file)
                decrypt_file(file_path, fernet)

# Replace with your actual encryption key here
encryption_key = b"kmMU1OSuZbc7movEo7oNOngg_mDKj7ZYjZHdjc0cHtQ="  # Use the exact key
fernet = Fernet(encryption_key)

# Folder path where your encrypted files are stored
folder_path = './test_encryption'

# Start decrypting files
decrypt_folder(folder_path, fernet)
print("Decryption completed.")


