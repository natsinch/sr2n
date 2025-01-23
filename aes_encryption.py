""" import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from utils import show_image
from utils import display_hacking_graphics

# ข้อความที่เข้ารหัสไว้ (ciphertext) สมมุติว่าเราได้มันมาจากการเข้ารหัส
ciphertext = base64.b64decode("roF4bu09FX2WjJV5B6SqME344dYu9bZXjSKhe1oUGQg=")

# ข้อความที่เราคาดหวังจะได้จากการถอดรหัส
expected_plaintext = "Parin Sornlertlamvanich"

# ฟังก์ชันเพื่อทำ AES Decryption
def aes_decrypt(key, iv, ciphertext):
    try:
        # สร้าง Cipher
        cipher = AES.new(key, AES.MODE_CBC, iv)
        # ถอดรหัสและลบ padding
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')
        return decrypted
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการถอดรหัส: {e}")
        return None

def aes_task():
    while True:
        # คำใบ้สำหรับการหาค่า Key และ IV (จากภาพ)
        print("Hint: You can contact me without h")
        show_image("images/hint11.png")
        key_input = input("Please enter the Key (16 bytes): ").encode('utf-8')  # ผู้เล่นกรอก Key
        
        print("Hint: Engineering student shirt colors")
        show_image("images/hint12.jpg") 
        iv_input = input("Please enter the IV (16 bytes): ").encode('utf-8')    # ผู้เล่นกรอก IV

        # ถอดรหัสข้อความ
        decrypted_text = aes_decrypt(key_input, iv_input, ciphertext)

        if decrypted_text == expected_plaintext:
            display_hacking_graphics()
            print(f"Successfully decrypted AES: Key={key_input}, IV={iv_input}")
            print(f"Decrypted message: {decrypted_text}")
            return key_input, iv_input
        
        else:
            print("\n[Hack Failed] Incorrect inputs! Please try again.\n")

        

# เรียกใช้งานฟังก์ชัน
#aes_task()
 """

import time
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from utils import show_image
from utils import display_hacking_graphics

# ข้อความที่เข้ารหัสไว้ (ciphertext) สมมุติว่าเราได้มันมาจากการเข้ารหัส
ciphertext = base64.b64decode("roF4bu09FX2WjJV5B6SqME344dYu9bZXjSKhe1oUGQg=")

# ข้อความที่เราคาดหวังจะได้จากการถอดรหัส
expected_plaintext = "Parin Sornlertlamvanich"

# ฟังก์ชันเพื่อทำ AES Decryption
def aes_decrypt(key, iv, ciphertext):
    try:
        # สร้าง Cipher
        cipher = AES.new(key, AES.MODE_CBC, iv)
        # ถอดรหัสและลบ padding
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')
        return decrypted
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการถอดรหัส: {e}")
        return None

def aes_task():
    while True:
        # คำใบ้สำหรับการหาค่า Key และ IV (จากภาพ)
        print("Hint: Mr.P You can contact him without h")
        show_image("images/hint11.png")
        print("Hint:UTF-8")
        key_input = input("Please enter the Key (16 bytes): ").encode('utf-8')  # ผู้เล่นกรอก Key
        
        print("Hint: Engineering student shirt colors")
        show_image("images/hint12.jpg") 
        print("Hint:UTF-8")
        iv_input = input("Please enter the IV (16 bytes): ").encode('utf-8')    # ผู้เล่นกรอก IV

        # ถอดรหัสข้อความ
        decrypted_text = aes_decrypt(key_input, iv_input, ciphertext)

        if decrypted_text == expected_plaintext:
            ##display_hacking_graphics()###
            print(f"It's correct, here you go: Key={key_input}, IV={iv_input}")
            # print(f"Decrypted message: {decrypted_text}")
            time.sleep(2)
            print("Find the password that has been encrypted using the provided KEY and IV!\n")
            print("Hint: The encryption mode that links each data block together, think of each block referencing the previous block.\n")
            time.sleep(1)
            print(f"This is encrypted message = roF4bu09FX2WjJV5B6SqME344dYu9bZXjSKhe1oUGQg=")

            # วนลูปจนกว่าผู้เล่นจะกรอกรหัสผ่านที่ถูกต้อง
            while True:
                passdecrypt = input("Please enter the decrypted message: ")

                if passdecrypt == expected_plaintext:
                    display_hacking_graphics()
                    print(f"Successfully! Decrypted message is: {passdecrypt}")
                    break  # ออกจากลูปเมื่อกรอกรหัสผ่านถูกต้อง
                else:
                    print("\n[Hack Failed] Incorrect decrypted password! Please try again.\n")

            return key_input, iv_input, passdecrypt
        
        else:
            print("\n[Hack Failed] Incorrect inputs! Please try again.\n")

# เรียกใช้งานฟังก์ชัน
#aes_task()


