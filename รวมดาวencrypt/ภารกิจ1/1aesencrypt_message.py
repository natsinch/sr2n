import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# ฟังก์ชันเข้ารหัส AES
def aes_encrypt(key, iv, plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(ciphertext).decode()

# กำหนดข้อความ, คีย์, และ IV
plaintext = "Parin Sornlertlamvanich"
key = b"parin.s@sut.ac.t"  # คีย์ 16 bytes ที่กำหนดเอง
iv = b"cybersecurity267"   # IV 16 bytes ที่กำหนดเอง

# เข้ารหัสข้อความ
encrypted_message = aes_encrypt(key, iv, plaintext)

# บันทึกไฟล์ที่เก็บข้อความที่เข้ารหัส
with open("locked_file_with_aes.bin", "w") as file:
    file.write(encrypted_message)

print("ไฟล์ที่เข้ารหัส AES ถูกสร้างเสร็จเรียบร้อยแล้ว!")
