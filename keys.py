import os
import pickle

def save_key_to_file(filename, key):
    with open(filename, 'wb') as f:
        pickle.dump(key, f)

def load_key_from_file(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def generate_key_pair():
    private_key = os.urandom(16)  # Простой пример генерации ключа
    public_key = os.urandom(16)  # Для учебных целей
    return private_key, public_key

private_key_file = "private_key.pem"
public_key_file = "public_key.pem"

if not os.path.exists(private_key_file) or not os.path.exists(public_key_file):
    private_key, public_key = generate_key_pair()
    save_key_to_file(private_key_file, private_key)
    save_key_to_file(public_key_file, public_key)
else:
    private_key = load_key_from_file(private_key_file)
    public_key = load_key_from_file(public_key_file)

print("Ключи успешно загружены или сгенерированы.")