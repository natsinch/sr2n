import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
from utils import show_image, display_hacking_graphics
import time


# ฟังก์ชันถอดรหัส RSA
def rsa_decrypt(private_key, encrypted_message):
    try:
        key = RSA.import_key(private_key)
        cipher_rsa = PKCS1_OAEP.new(key)
        decrypted_message = cipher_rsa.decrypt(encrypted_message)
        return decrypted_message.decode()
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการถอดรหัส: {e}")
        return None

# ฟังก์ชันเพื่อปลดล็อคไฟล์ (ใช้เลขจากคำใบ้)
def unlock_file_using_hint(hint_number):
    locked_file_path = "locked_file_with_private_key.bin"
    if hint_number == 34:  # คำตอบที่ถูกต้องจากคำใบ้
        if os.path.exists(locked_file_path):
            with open(locked_file_path, "rb") as file:
                private_key = file.read()
            return private_key
        else:
            print("ไม่พบไฟล์ที่ถูกล็อค!")
            return None
    else:
        print("\nคำตอบไม่ถูกต้อง! ไม่สามารถปลดล็อคไฟล์ได้.\n")
        return None

# ภารกิจที่ 2
def rsa_task():
    print("-" * 60)

    # แสดงคำใบ้
    show_image("images/hint2.jpg")

    private_key = None

    # รับ input เพื่อปลดล็อคไฟล์
    while not private_key:
        try:
            hint_number = int(input("กรุณากรอกรหัสผ่านเพื่อปลดล็อคไฟล์ (ตัวเลข 2 ตัว): "))
            private_key = unlock_file_using_hint(hint_number)
            if not private_key:
                print("[ล้มเหลว] กรุณาลองอีกครั้ง.")
        except ValueError:
            print("[ล้มเหลว] กรุณากรอกตัวเลขที่ถูกต้อง!")

    print("\n[ปลดล็อคสำเร็จ!] Private Key ที่ปลดล็อคได้:")
    time.sleep(2)
    print(private_key.decode())
    time.sleep(2)
    # อ่านข้อความที่เข้ารหัส
    with open("encrypted_message.txt", "r") as file:
        encrypted_message = base64.b64decode(file.read())
    print("\n[ข้อความที่ถูกเข้ารหัส]:", base64.b64encode(encrypted_message).decode())

    # รับข้อความที่ถอดรหัสจากผู้ใช้
    decrypted_message = rsa_decrypt(private_key, encrypted_message)
    if not decrypted_message:
        print("[ล้มเหลว] การถอดรหัสผิดพลาด!")
        return False

    while True:
        player_input = input("กรุณาป้อนข้อความที่ถอดรหัสได้: ").strip()
        if player_input == decrypted_message:
            display_hacking_graphics()
            print("[สำเร็จ!] คุณผ่านภารกิจที่ 2!")
            return True
        else:
            print("[ล้มเหลว] ข้อความไม่ตรงกัน กรุณาลองอีกครั้ง.")

# เรียกใช้งานฟังก์ชัน
#if __name__ == "__main__":
#    rsa_task()
