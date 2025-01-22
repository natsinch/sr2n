import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

# ฟังก์ชันเข้ารหัส AES
def aes_encrypt(key, iv, plaintext):
    # ไม่ต้องแปลง key และ iv เป็น bytes เพราะมันเป็น bytes อยู่แล้ว
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(ciphertext).decode()

# สร้างข้อความและคีย์
plaintext = "Hello Hacker!!"
key = b"comenisintrovert"  # คีย์ 16 bytes สำหรับ AES (ต้องเป็น bytes)
iv = b"ilovesCyberSecue"   # IV 16 bytes สำหรับ AES (ต้องเป็น bytes)

# เข้ารหัสข้อความ
encrypted_message = aes_encrypt(key, iv, plaintext)

# บันทึกไฟล์ที่เก็บข้อความที่เข้ารหัส
with open("locked_file_with_aes.bin", "w") as file:
    file.write(encrypted_message)

print("ไฟล์ที่เข้ารหัส AES ถูกสร้างเสร็จเรียบร้อยแล้ว!")

