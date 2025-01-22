import hashlib
from utils import show_image
from utils import display_hacking_graphics

# ข้อความที่ถูกแฮช
hashed_password = hashlib.sha256("CPESUT".encode()).hexdigest()

def hash_task():
    print("-" * 60)
    print("คำใบ้: หาข้อความที่ซ่อนอยู่ในรูป")
    show_image("images/hashHint.png")
    print("คุณต้องกรอกรหัสผ่านเพื่อไปยังภารกิจถัดไป!!")
    
    # รับค่าแฮชจากผู้ใช้
    while True:
        user_hash = input("กรอกรหัสที่คิดว่าเป็นคำตอบ: ").strip()
        if user_hash == hashed_password:
            display_hacking_graphics()
            print("ค่า hash ถูกต้อง! เข้าภารกิจถัดไป.")
            return True
        else:
            print("ค่า hash ไม่ถูกต้อง! ลองใหม่อีกครั้ง.")

# เรียกใช้งานฟังก์ชัน
#hash_task()
