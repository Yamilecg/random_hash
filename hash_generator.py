import random
import string
import hashlib

def random_hash():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(32))

def main():
    for _ in range(1000):
        h = hashlib.md5(random_hash().encode()).hexdigest()
        if h.startswith("00"):
            print(f"Hash encontrado: {h}")
            return True
    print("No se encontró ningún hash que empiece con 00")
    return False

if __name__ == "__main__":
    main()
