import hashlib
from utils import show_image
from utils import display_hacking_graphics

# ข้อความที่ถูกแฮช
hashed_password = hashlib.sha256("CPESUT".encode()).hexdigest()

def hash_task():
    print("ภารกิจ 3: เปิดเผยรหัสผ่านจากการแฮช!")
    print("คำใบ้: หาคำตอบที่ซ่อนอยู่เพื่อหาค่าแฮชมาเปรียบเทียบรหัสผ่าน")
    show_image("images/hashHint.png")
    
    # รับค่าแฮชจากผู้ใช้
    while True:
        user_hash = input("กรอกรหัสที่คิดว่าเป็นคำตอบ: ").strip()
        if user_hash == hashed_password:
            print("ค่าแฮชถูกต้อง! เข้าภารกิจถัดไป.")
            display_hacking_graphics()
            return False
        else:
            print("ค่าแฮชไม่ถูกต้อง! ลองใหม่อีกครั้ง.")

# เรียกใช้งานฟังก์ชัน
hash_task()
