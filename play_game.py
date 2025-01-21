import time
from aes_encryption import aes_task
from rsa_encryption import rsa_task
from hash_challenge import hash_task
from final_mission import final_task
from utils import display_hacking_graphics, print_story

# ฟังก์ชันที่ใช้ในการตรวจสอบผลลัพธ์ของแต่ละภารกิจ
def play_game():
    print("=" * 60)
    print("ยินดีต้อนรับสู่ Crypto Heist!")
    print("คุณคือ The Cipher Ghost แฮ็กเกอร์ระดับตำนาน")
    print("ภารกิจของคุณ: แฮ็กระบบธนาคารและขโมยรหัสลับให้สำเร็จ")
    print("=" * 60)
    time.sleep(2)

    # บทนำเนื้อเรื่อง
    print("\n[บทนำ] เริ่มต้นภารกิจของคุณ...")
    print_story()
    time.sleep(5)

    # Mission 1: AES (หา KEY และ IV)
    print("\n[ภารกิจที่ 1: ถอดรหัส AES]")
    print("เป้าหมาย: ปลดล็อกชั้นแรกของระบบที่ถูกเข้ารหัสด้วย AES")
    print("ทดสอบทักษะการแฮ็กของคุณ!")
    display_hacking_graphics()
    
    # ตรวจสอบผลลัพธ์ของภารกิจ 1
    if not aes_task():  
        print("\n[ล้มเหลว] คุณไม่สามารถถอดรหัส AES ได้! ลองใหม่อีกครั้ง.")
        return  # หยุดเกมหากภารกิจแรกไม่สำเร็จ

    print("\n[สำเร็จ!] คุณถอดรหัส AES ได้สำเร็จ")
    time.sleep(2)

    # Mission 2: RSA
    print("\n[ภารกิจที่ 2: ปลดล็อก RSA]")
    print("เป้าหมาย: ค้นหา Private Key ที่ซ่อนอยู่ในไฟล์ลับ และใช้มันเพื่อถอดรหัสข้อความสำคัญ")
    print("คอยระวังระบบรักษาความปลอดภัย...")
    display_hacking_graphics()
    
    # ตรวจสอบผลลัพธ์ของภารกิจ 2
    if not rsa_task():  
        print("\n[ล้มเหลว] คุณไม่สามารถถอดรหัส RSA ได้! ลองใหม่อีกครั้ง.")
        return  # หยุดเกมหากภารกิจที่ 2 ไม่สำเร็จ

    print("\n[สำเร็จ!] คุณถอดรหัส RSA ได้สำเร็จ")
    time.sleep(2)

    # Mission 3: Hash
    print("\n[ภารกิจที่ 3: เปิดเผยรหัสผ่านด้วย Hash]")
    print("เป้าหมาย: แกะรหัสผ่านที่ถูกแฮชไว้เพื่อเข้าถึงระบบขั้นสูงสุด")
    print("ระมัดระวังทุกตัวอักษร...")
    display_hacking_graphics()
    
    # ตรวจสอบผลลัพธ์ของภารกิจ 3
    if not hash_task():  
        print("\n[ล้มเหลว] คุณไม่สามารถแกะรหัส Hash ได้! ลองใหม่อีกครั้ง.")
        return  # หยุดเกมหากภารกิจที่ 3 ไม่สำเร็จ

    print("\n[สำเร็จ!] คุณแกะรหัส Hash ได้สำเร็จ")
    time.sleep(2)

    # Final Mission
    print("\n[ภารกิจที่ 4: ศึกสุดท้าย]")
    print("คุณมาถึงระบบส่วนกลางที่ถูกป้องกันด้วยการเข้ารหัสหลายชั้น")
    print("นี่คือความท้าทายสุดท้าย! ใช้ทุกทักษะที่มีเพื่อแฮ็กระบบนี้ให้สำเร็จ!")
    print("พยายามให้เร็วที่สุดและระมัดระวังการตรวจจับจากระบบรักษาความปลอดภัย!")
    display_hacking_graphics()
    
    # ตรวจสอบผลลัพธ์ของภารกิจสุดท้าย
    final_task()

    # ตอนจบ
    print("\n[ตอนจบ] การแฮ็กเสร็จสมบูรณ์!")
    print("ยินดีด้วย! คุณปลดล็อกระบบธนาคารสำเร็จและขโมยเงินล้านได้สำเร็จ!")
    print("ชื่อของคุณจะถูกจารึกในตำนานของโลกใต้ดินไซเบอร์... The Cipher Ghost!")
    print("\n[Crypto Heist: Mission Accomplished]")
    print("=" * 60)

if __name__ == "__main__":
    play_game()
