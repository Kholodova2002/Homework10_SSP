import socket
import pickle
from keys import load_key_from_file
HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)

print("Сервер ожидает подключения...")
conn, addr = sock.accept()
print(f"Подключение от {addr}")

# Загрузка ключей
private_key = load_key_from_file("private_key.pem")
public_key = load_key_from_file("public_key.pem")

# Получаем публичный ключ клиента
client_public_key = pickle.loads(conn.recv(1024))
print(f"Получен публичный ключ клиента: {client_public_key}")

# Отправляем публичный ключ сервера клиенту
conn.send(pickle.dumps(public_key))

# Получаем зашифрованное сообщение от клиента
encrypted_message = conn.recv(1024)
print(f"Получено зашифрованное сообщение: {encrypted_message}")

# Расшифровываем сообщение с использованием приватного ключа
decrypted_message = bytes([b ^ private_key[0] for b in encrypted_message])
print(f"Расшифрованное сообщение: {decrypted_message.decode()}")

conn.close()