from Crypto.PublicKey import RSA

# สร้าง RSA Keypair
key = RSA.generate(2048)

# รับ Private Key และ Public Key
private_key = key.export_key()
public_key = key.publickey().export_key()

# บันทึก Private Key ลงในไฟล์
with open("locked_file_with_private_key.bin", "wb") as file:
    file.write(private_key)

print("ไฟล์ที่เก็บ Private Key ถูกสร้างเสร็จเรียบร้อยแล้ว!")

with open("locked_file_with_public_key.bin", "wb") as file:
    file.write(public_key)

print("ไฟล์ที่เก็บ Public Key ถูกสร้างเสร็จเรียบร้อยแล้ว!")