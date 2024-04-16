import socket
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def encrypt_message(message, public_key):
    encrypted_message = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_message

def load_server_public_key():
    try:
        with open("hacked_key.pem", "rb") as key_file:  # Load the correct server's public key
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
        return public_key
    except Exception as e:
        print(f"Error loading public key: {e}")
        return None

def main():
    public_key = load_server_public_key()
    if not public_key:
        return  # Exit if public key loading failed

    # Establish connection with server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 12345))

        while True:
            client_message = input("Client message: ")

            encrypted_client_message = encrypt_message(client_message, public_key)

            print("-----------:Encrypted message:--------------")
            print(encrypted_client_message)
            print("------------------:end:---------------------")

            # Send length of data before sending actual data
            s.sendall(len(encrypted_client_message).to_bytes(4, 'big'))
            s.sendall(encrypted_client_message)

            if client_message.lower() == "exit":
                break

            # Receive and print response from server
            encrypted_server_message_length = int.from_bytes(s.recv(4), 'big')
            encrypted_server_message = s.recv(encrypted_server_message_length)

            if not encrypted_server_message:
                break

            print("Encrypted Server message:", encrypted_server_message)


if __name__ == "__main__":
    main()
