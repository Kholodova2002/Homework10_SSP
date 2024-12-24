import socket
import pickle
from keys import load_key_from_file
HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

# Загрузка ключей
private_key = load_key_from_file("private_key.pem")
public_key = load_key_from_file("public_key.pem")

# Отправляем публичный ключ серверу
sock.send(pickle.dumps(public_key))

# Получаем публичный ключ сервера
server_public_key = pickle.loads(sock.recv(1024))
print(f"Получен публичный ключ сервера: {server_public_key}")

# Шифруем сообщение с использованием публичного ключа сервера
message = b"Hello, secure world!"
encrypted_message = bytes([b ^ server_public_key[0] for b in message])
sock.send(encrypted_message)

sock.close()