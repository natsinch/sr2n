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
        print("\nIncorrect password! Unable to unlock the file.\n")
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
            hint_number = int(input("Please enter the password to unlock the file. (Hint: Two digits): "))
            private_key = unlock_file_using_hint(hint_number)
            if not private_key:
                print("[Failed] Please try again.")
        except ValueError:
            print("[Failed] Please enter the correct password!")

    print("\n[Unlock successful!] Here is the data in the unlocked file:")
    time.sleep(2)
    print(private_key.decode())
    time.sleep(2)
    # อ่านข้อความที่เข้ารหัส
    with open("encrypted_message.txt", "r") as file:
        encrypted_message = base64.b64decode(file.read())
    print("\n[Encrypted message]:", base64.b64encode(encrypted_message).decode())

    # รับข้อความที่ถอดรหัสจากผู้ใช้
    decrypted_message = rsa_decrypt(private_key, encrypted_message)
    if not decrypted_message:
        print("[Failed] Decryption error!")
        return False

    while True:
        player_input = input("Please enter the decrypted message: ").strip()
        if player_input == decrypted_message:
            display_hacking_graphics()
            print("[Success!] You have completed Mission 2!")
            return True
        else:
            print("[Failed] The message does not match. Please try again.")

# เรียกใช้งานฟังก์ชัน
#if __name__ == "__main__":
#    rsa_task()
