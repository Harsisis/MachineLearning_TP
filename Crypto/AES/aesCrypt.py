from Crypto.Cipher import AES
from dotenv import load_dotenv
import os

load_dotenv()

# Get secret from environnement var
SECRET_AES = (os.getenv('SECRET_AES'))
# Get file from environnement var
FILE = (os.getenv('FILE'))
# Get file from environnement var
TARGET_FILE = (os.getenv('TARGET_FILE'))
# Get file from environnement var
DECRYPT_FILE = (os.getenv('DECRYPT_FILE'))

with open(FILE, 'rb') as file_in, open(TARGET_FILE, 'wb') as file_out, open(DECRYPT_FILE, 'wb') as file_clear:
    from Crypto.Cipher import AES

    data = file_in.read()

    e_cipher = AES.new(SECRET_AES.encode(), AES.MODE_EAX)
    e_data = e_cipher.encrypt(data)
    file_out.write(e_data)

    d_cipher = AES.new(SECRET_AES.encode(), AES.MODE_EAX, e_cipher.nonce)
    d_data = d_cipher.decrypt(e_data)
    file_clear.write(d_data)

    print("Encryption was : ", e_data)
    print("Original Message was : ", d_data)
