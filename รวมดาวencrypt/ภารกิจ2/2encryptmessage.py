from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64

# โหลด Public Key จากคู่ที่สร้างในขั้นก่อนหน้า
with open("locked_file_with_private_key.bin", "rb") as file:
    private_key = RSA.import_key(file.read())
    public_key = private_key.publickey()

# สร้างข้อความ
plaintext = "Secrets for mission 2"

# เข้ารหัสข้อความ
cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted_message = cipher_rsa.encrypt(plaintext.encode())
print(encrypted_message)
# บันทึกข้อความที่เข้ารหัสในรูป Base64
with open("encrypted_message.txt", "w") as file:
    file.write(base64.b64encode(encrypted_message).decode())

print("ข้อความที่เข้ารหัสถูกสร้างและบันทึกแล้ว!")

