from Crypto.PublicKey import RSA

# สร้าง RSA Keypair
key = RSA.generate(2048)

# Export Private Key
private_key = key.export_key()

# บันทึก Private Key ลงในไฟล์
with open("locked_file_with_private_key.bin", "wb") as file:
    file.write(private_key)

print("ไฟล์ locked_file_with_private_key.bin ถูกสร้างแล้ว!")
