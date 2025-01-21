import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from utils import show_image

# ข้อความที่เข้ารหัสไว้ (ciphertext) สมมุติว่าเราได้มันมาจากการเข้ารหัส
ciphertext = base64.b64decode("ekzO2yNTve1jhLKWpBoebA==")

# ข้อความที่เราคาดหวังจะได้จากการถอดรหัส
expected_plaintext = "Hello Hacker!!"

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

# ฟังก์ชันตรวจสอบขนาดของ Key และ IV
def check_key_iv(key, iv):
    if len(key) != 16:
        print(f"ข้อผิดพลาด: Key ต้องมีขนาด 16 bytes แต่มีขนาด {len(key)} bytes")
        return False
    if len(iv) != 16:
        print(f"ข้อผิดพลาด: IV ต้องมีขนาด 16 bytes แต่มีขนาด {len(iv)} bytes")
        return False
    return True

def aes_task():
    print("🚨 แผนการเจาะระบบธนาคารเริ่มต้นขึ้น! 🚨")
    print("เป้าหมายของคุณคือการเจาะระบบเพื่อถอดรหัสข้อความลับ และใช้ข้อมูลเพื่อโอนเงินออกจากธนาคาร.")
    
    print("[แสดงภาพคำใบ้ของ Key...]")
    show_image("photo/hint1.jpg")  # แสดงภาพคำใบ้แรก
    key_input = input("🔑 กรุณาป้อน Key (16 bytes): ").encode('utf-8')
    
    print("[แสดงภาพคำใบ้ของ IV...]")
    show_image("photo/hint2.jpg")  # แสดงภาพคำใบ้อีกครั้ง
    iv_input = input("🗝️ กรุณาป้อน IV (16 bytes): ").encode('utf-8')

    print("[แฮ็กข้อมูล... 0%]")
    print("[แฮ็กข้อมูล... 25%]")
    print("[แฮ็กข้อมูล... 50%]")
    print("[แฮ็กข้อมูล... 75%]")
    print("[แฮ็กข้อมูล... 100%]")

    # ตรวจสอบขนาดของ Key และ IV
    if not check_key_iv(key_input, iv_input):
        print("❌ การแฮ็กล้มเหลว: Key หรือ IV ไม่ถูกต้อง!")
        return None, None

    # ถอดรหัสข้อความ
    decrypted_text = aes_decrypt(key_input, iv_input, ciphertext)
    
    # แสดงผลลัพธ์ที่ถอดรหัส
    if decrypted_text:
        print(f"✅ ข้อความที่ถอดรหัสได้: {decrypted_text}")
        
    # เปรียบเทียบข้อความที่ถอดรหัสได้กับ expected_plaintext
    if decrypted_text == expected_plaintext:
        print("💸 [แฮ็กสำเร็จ!] คุณสามารถเข้าถึงระบบธนาคารได้แล้ว!")
        print(f"🎉 ใช้ Key: {key_input.decode('utf-8')} และ IV: {iv_input.decode('utf-8')} เพื่อโอนเงินออกจากระบบ.")
        print("📄 ข้อมูลถูกบันทึกและโอนเงินสำเร็จ.")
        return key_input, iv_input
    else:
        print("🚨 [การแฮ็กล้มเหลว!] ค่าที่ป้อนไม่ถูกต้อง.")
        return None, None

# เรียกใช้งานฟังก์ชัน
aes_task()
