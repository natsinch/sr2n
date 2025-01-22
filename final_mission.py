""" import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from utils import show_image
from utils import display_hacking_graphics

# ข้อความที่เข้ารหัสไว้ (ciphertext) สมมุติว่าเราได้มันมาจากการเข้ารหัส
ciphertext = base64.b64decode("ekzO2yNTve1jhLKWpBoebA==")

# ข้อความที่เราคาดหวังจะได้จากการถอดรหัส
expected_plaintext = "Hello Hacker!!"

# ฟังก์ชันเพื่อทำ AES Decryption
def final_decrypt(key, iv, ciphertext):
    try:
        # สร้าง Cipher
        cipher = AES.new(key, AES.MODE_CBC, iv)
        # ถอดรหัสและลบ padding
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')
        return decrypted
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการถอดรหัส: {e}")
        return None

# ฟังก์ชันตรวจสอบขนาดของ Key และ IV
def check_key_iv(key, iv):
    if len(key) != 16:
        print(f"Error: Key must be 16 bytes, but it is {len(key)} bytes.")
        return False
    if len(iv) != 16:
        print(f"Error: IV must be 16 bytes, but it is {len(iv)} bytes.")
        return False
    return True

def final_task():
    print("-" * 60)
    print("Your objective is to infiltrate the system, decrypt the secret message, and use the information to transfer funds from the bank.")
    
    while True:
        print("[Displaying hint for the Key...]")
        show_image("images/hint41.jpg")  # แสดงภาพคำใบ้แรก
        key_input = input("🔑 Please enter the Key (16 bytes): ").encode('utf-8')
        
        print("[Displaying hint for the IV...]]")
        show_image("images/hint42.jpg")  # แสดงภาพคำใบ้อีกครั้ง
        iv_input = input("🗝️ Please enter the IV (16 bytes): ").encode('utf-8')

        # ตรวจสอบขนาดของ Key และ IV
        if check_key_iv(key_input, iv_input):
            break  # หาก Key และ IV ถูกต้อง ออกจากลูป
        print("❌ Hack failed: Incorrect Key or IV! Please try again.")

    # ถอดรหัสข้อความ
    decrypted_text = final_decrypt(key_input, iv_input, ciphertext)
    
    # แสดงผลลัพธ์ที่ถอดรหัส
    if decrypted_text:
        print(f"✅ Decrypted message: {decrypted_text}")
        
    # เปรียบเทียบข้อความที่ถอดรหัสได้กับ expected_plaintext
    if decrypted_text == expected_plaintext:
        display_hacking_graphics()
        print("💸 You have successfully accessed the bank system!")
        print(f"🎉 Use Key: {key_input.decode('utf-8')} and IV: {iv_input.decode('utf-8')} to transfer funds from the system.")
        print("📄 Data has been recorded, and the transfer was successful.")
        return key_input, iv_input
    else:
        print("🚨 [Hack failed!] Incorrect inputs.")
        return None, None

# เรียกใช้งานฟังก์ชัน
#if __name__ == "__main__":
#    final_task()

 """
import time
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from utils import show_image
from utils import display_hacking_graphics

# ข้อความที่เข้ารหัสไว้ (ciphertext) สมมุติว่าเราได้มันมาจากการเข้ารหัส
ciphertext = base64.b64decode("ekzO2yNTve1jhLKWpBoebA==")

# ข้อความที่เราคาดหวังจะได้จากการถอดรหัส
expected_plaintext = "Hello Hacker!!"

# ฟังก์ชันเพื่อทำ AES Decryption
def final_decrypt(key, iv, ciphertext):
    try:
        # สร้าง Cipher
        cipher = AES.new(key, AES.MODE_CBC, iv)
        # ถอดรหัสและลบ padding
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')
        return decrypted
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการถอดรหัส: {e}")
        return None

# ฟังก์ชันตรวจสอบขนาดของ Key และ IV
def check_key_iv(key, iv):
    if len(key) != 16:
        print(f"Error: Key must be 16 bytes, but it is {len(key)} bytes.")
        return False
    if len(iv) != 16:
        print(f"Error: IV must be 16 bytes, but it is {len(iv)} bytes.")
        return False
    return True

def final_task():
    print("-" * 60)
    print("Your objective is to infiltrate the system, decrypt the secret message, and use the information to transfer funds from the bank.")
    
    while True:
        print("[Displaying hint for the Key...]")
        show_image("images/hint41.jpg")  # แสดงภาพคำใบ้แรก
        key_input = input("🔑 Please enter the Key (16 bytes): ").encode('utf-8')
        
        print("[Displaying hint for the IV...]]")
        show_image("images/hint42.jpg")  # แสดงภาพคำใบ้อีกครั้ง
        iv_input = input("🗝️ Please enter the IV (16 bytes): ").encode('utf-8')

        # ตรวจสอบขนาดของ Key และ IV
        if check_key_iv(key_input, iv_input):
            break  # หาก Key และ IV ถูกต้อง ออกจากลูป
        print("❌ Hack failed: Incorrect Key or IV! Please try again.")

    # ถอดรหัสข้อความ
    decrypted_text = final_decrypt(key_input, iv_input, ciphertext)
    
    # แสดงผลลัพธ์ที่ถอดรหัส
    #if decrypted_text:
        #print(f"✅ Decrypted message: {decrypted_text}")
        
    # เปรียบเทียบข้อความที่ถอดรหัสได้กับ expected_plaintext
    if decrypted_text == expected_plaintext:
        #display_hacking_graphics()
        print("💸 You have successfully accessed the bank system!")
        print(f"🎉 Use Key: {key_input.decode('utf-8')} and IV: {iv_input.decode('utf-8')} to transfer funds from the system.")
        time.sleep(2)
        print("Find the last password that has been encrypted to proceed successfully using the provided KEY and IV!\n")
        print("Hint: The encryption mode that links each data block together, think of each block referencing the previous block.\n")
        time.sleep(1)
        print(f"This is encrypted password = ekzO2yNTve1jhLKWpBoebA==")
        passdecrypt=input("Please enter the decrypted password: ")
        if passdecrypt == expected_plaintext:
                display_hacking_graphics()
                print(f"🎉 It's correct! The lass password is: {passdecrypt}")
        print("📄 Data has been recorded, and the transfer was successful.")
        return key_input, iv_input, passdecrypt
    else:
        print("🚨 [Hack failed!] Incorrect inputs.")
        return None, None

# เรียกใช้งานฟังก์ชัน
if __name__ == "__main__":
    final_task()

