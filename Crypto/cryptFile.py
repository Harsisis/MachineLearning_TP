import base64
import hashlib, hmac
import os
from dotenv import load_dotenv

load_dotenv()

# Get secret from environnement var
SECRET = (os.getenv('SECRET'))
# Get file from environnement var
FILE = (os.getenv('FILE'))

def encrypt():
    with open(FILE, "rb") as f:
        mac1 = hmac.HMAC(SECRET.encode(), digestmod=hashlib.sha512)
        digest = hashlib.file_digest(f, lambda: mac1)
    print(digest.hexdigest())
    
encrypt()