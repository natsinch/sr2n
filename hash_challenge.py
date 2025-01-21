import hashlib

# ข้อความที่ถูกแฮช
hashed_password = hashlib.sha256("CPESUT".encode()).hexdigest()

def hash_task():
    print("ภารกิจ 3: เปิดเผยรหัสผ่านจากการแฮช!")
    print("คำใบ้: หาคำตอบที่ซ่อนอยู่เพื่อหาค่าแฮชมาเปรียบเทียบรหัสผ่าน")
    
    # รับค่าแฮชจากผู้ใช้
    user_hash = input("กรอกรหัสที่คิดว่าเป็นคำตอบ: ").strip()
    
    # # แสดงข้อมูลเพื่อดีบัก (ช่วยตรวจสอบ)
    # print(f"hashed_password: {hashed_password}")
    # print(f"user_hash: {user_hash}")
    
    # เปรียบเทียบค่าแฮชที่ผู้ใช้ป้อนกับค่าแฮชที่ถูกต้อง
    
    if user_hash == hashed_password:
        print("ค่าแฮชถูกต้อง! เข้าภารกิจถัดไป.")
    else:
        print("ค่าแฮชไม่ถูกต้อง! ลองใหม่อีกครั้ง.")

# เรียกใช้งานฟังก์ชัน
hash_task()
