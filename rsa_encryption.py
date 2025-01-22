import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
from utils import show_image
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
        print("คำตอบไม่ถูกต้อง! ไม่สามารถปลดล็อคไฟล์ได้.")
        return None

# ภารกิจที่ 2
def rsa_task():
    # เพิ่มเนื้อเรื่องของภารกิจ
    print("=" * 60)
    print("ภารกิจที่ 2: ปลดล็อกรหัส RSA")
    print(
        "หลังจากที่คุณผ่านระบบเข้ารหัส AES มาได้สำเร็จ คุณถูกนำตัวไปยังห้องที่มีระบบป้องกันข้อมูลแบบ RSA-2048\n"
        "ระบบได้ทำการเข้ารหัสข้อมูลสำคัญ โดยแยกคีย์ส่วนตัวออกเป็นชิ้นส่วนและซ่อนอยู่ในเอกสารลับ.\n"
        "คำใบ้ในภาพด้านล่างจะช่วยให้คุณค้นหา Private Key ได้.\n"
        "เมื่อได้ Private Key มาแล้ว คุณจะต้องใช้เพื่อถอดรหัสข้อความที่ซ่อนอยู่.\n"
    )
    print("=" * 60)
    show_image("images/hint2.jpg")  # แสดงภาพคำใบ้

    try:
        hint_number = int(input("กรุณากรอกรหัสผ่านเพื่อปลดล็อคไฟล์ (ตัวเลข 2 ตัว): "))

        private_key = unlock_file_using_hint(hint_number)

        if private_key:
            print("\n[ปลดล็อคสำเร็จ!]")

            print("[Private Key ที่ปลดล็อคได้]:")
            print(private_key.decode())

            # อ่านข้อความที่เข้ารหัสจากไฟล์
            with open("encrypted_message.txt", "r") as file:
                encrypted_message = base64.b64decode(file.read())

            print("\n[ข้อความที่ถูกเข้ารหัส]:")
            print(base64.b64encode(encrypted_message).decode())

            # ให้ผู้เล่นใช้ Private Key เพื่อถอดรหัสข้อความ
            print(
                "\nกรุณาใช้ Private Key และข้อความที่ถูกเข้ารหัสข้างต้นเพื่อถอดรหัส.\n"
                "หลังจากถอดรหัสแล้ว ให้ป้อนข้อความที่คุณถอดได้."
            )
            player_input = input("กรุณาป้อนข้อความที่ถอดรหัสได้: ").strip()

            # ถอดรหัสข้อความเพื่อตรวจสอบคำตอบ
            decrypted_message = rsa_decrypt(private_key, encrypted_message)

            if player_input == decrypted_message:
                print("\n[สำเร็จ!] คุณผ่านภารกิจที่ 2!")
            else:
                print("\n[ล้มเหลว] ข้อความที่คุณป้อนไม่ตรงกับข้อความที่ถอดได้.")
        else:
            print("\n[ล้มเหลว] ไม่สามารถปลดล็อคไฟล์ได้.")
    except ValueError:
        print("\nกรุณากรอกตัวเลขที่ถูกต้อง!")
    except Exception as e:
        print(f"\nเกิดข้อผิดพลาด: {e}")

# เรียกใช้งานฟังก์ชัน
if __name__ == "__main__":
    rsa_task()

