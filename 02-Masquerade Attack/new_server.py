import socket
import time
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
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

def decrypt_message(encrypted_message, private_key):
    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message.decode()

def load_server_private_key():
    with open("server_private.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

def main():
    private_key = load_server_private_key()
    count = 0

    # Set up server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 12345))
        s.listen()

        print("Server listening...")
        while True:
            try:
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)

                    if count == 0:

                        # Receive client's public key
                        client_public_key_pem = conn.recv(4096)
                        client_public_key = serialization.load_pem_public_key(
                            client_public_key_pem,
                            backend=default_backend()
                        )

                        print("Client's Public Key:")
                        print(client_public_key.public_bytes(
                            encoding=serialization.Encoding.PEM,
                            format=serialization.PublicFormat.SubjectPublicKeyInfo
                        ).decode())

                        # Send server's public key to client
                        with open("server_public.pem", "rb") as key_file:
                            server_public_key = serialization.load_pem_public_key(
                                key_file.read(),
                                backend=default_backend()
                            )
                        conn.sendall(server_public_key.public_bytes(
                            encoding=serialization.Encoding.PEM,
                            format=serialization.PublicFormat.SubjectPublicKeyInfo
                        ))
                        count = 1

                    while True:
                        # Receive length of data first
                        encrypted_client_message_length = int.from_bytes(conn.recv(4), 'big')
                        encrypted_client_message = conn.recv(encrypted_client_message_length)

                        if not encrypted_client_message:
                            break

                        decrypted_client_message = decrypt_message(encrypted_client_message, private_key)

                        print("Client message: ", decrypted_client_message)

                        if decrypted_client_message.lower() == "exit":
                            break

                        time.sleep(2)
                        server_message = input("Server message: ")
                        encrypted_server_message = encrypt_message(server_message, client_public_key)
                        print("-----------:Encrypted message:--------------")
                        print(encrypted_server_message)
                        print("------------------:end:---------------------")

                        conn.sendall(len(encrypted_server_message).to_bytes(4, 'big'))
                        time.sleep(2)
                        conn.sendall(encrypted_server_message)

                    if decrypted_client_message.lower() == "exit":
                        break
            except Exception as e:
                print(f"An error occurred: {e}")
                continue

if __name__ == "__main__":
    main()
