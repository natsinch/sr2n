import time
from aes_encryption import aes_task
from rsa_encryption import rsa_task
from hash_challenge import hash_task
from final_mission import final_task
from utils import display_hacking_graphics, print_story, loading_animation

# ฟังก์ชันที่ใช้ในการตรวจสอบผลลัพธ์ของแต่ละภารกิจ
def play_game():
    print("=" * 60)
    print("Welcome to Crypto Heist!")
    print("You are The SR2N, a legendary hacker.")
    print("Your mission: Hack the banking system and steal the secret code successfully.")
    print("=" * 60)
    time.sleep(2)
    loading_animation()
    # บทนำเนื้อเรื่อง
    print("\n[Introduction] Starting your mission...")
    print_story()
# เรียกใช้งานฟังก์ชัน
    loading_animation()
    time.sleep(3)
    print("🚨 The plan to hack the banking system has begun! 🚨")
    
    # Mission 1: AES (หา KEY และ IV)
    print("=" * 60)
    print("[Mission 1: Decrypt AES]")
    print("Objective: Unlock the first layer of the system encrypted with AES.")
    print("Test your hacking skills!")
    print("-" * 60)
    time.sleep(3)
    # เรียกฟังก์ชัน aes_task() และเก็บผลลัพธ์
    
    aes_result = aes_task()
    
    # ตรวจสอบผลลัพธ์ของภารกิจ 1
    if not aes_result:  
        print("\n[Failed] You couldn't decrypt AES! Try again.")
        return  # หยุดเกมหากภารกิจแรกไม่สำเร็จ

    print("\n[Success!] You successfully decrypted AES.")
    print("=" * 60)
    print()
    
    loading_animation()
    print()
    time.sleep(2)

    # Mission 2: RSA
    print("=" * 60)
    print("[Mission 2: Unlock RSA]")
    print("Objective: Find the Private Key hidden in a secret file and use it to decrypt an important message.")
    print("Be cautious of security systems...")
    time.sleep(3)
    
    rsa_result = rsa_task()
    
    # ตรวจสอบผลลัพธ์ของภารกิจ 2
    if not rsa_result:  
        print("\n[Failed] You couldn't decrypt RSA! Try again.")
        return  # หยุดเกมหากภารกิจที่ 2 ไม่สำเร็จ

    print("\n[Success!] You successfully decrypted RSA.")
    print("=" * 60)
    print()
    loading_animation()
    print()
    time.sleep(2)

    # Mission 3: Hash
    print("=" * 60)
    print("[Mission 3: Reveal the password with SHA-256 Hash]")
    print("Objective: Break the hashed password to access the ultimate system.")
    print("Be careful with every character...")
    
    hash_result = hash_task()
    
    # ตรวจสอบผลลัพธ์ของภารกิจ 3
    if not hash_result:  
        print("\n[Failed] You couldn't break the Hash! Try again.")
        return  # หยุดเกมหากภารกิจที่ 3 ไม่สำเร็จ

    print("\n[Success!] You successfully broke the Hash.")
    print("=" * 60)
    print()
    loading_animation()
    print()
    time.sleep(2)
    

    # Final Mission
    print("=" * 60)
    print("[Mission 4: Final Battle]")
    print("You have reached the central system protected with multiple layers of encryption.")
    print("This is the ultimate challenge! Use all your skills to hack the system successfully!")
    print("Try to be as fast as possible and beware of detection by security systems!")
    
    # ตรวจสอบผลลัพธ์ของภารกิจสุดท้าย
    final_result = final_task()
    
    # ตรวจสอบผลลัพธ์ของภารกิจ 3
    if not final_result:  
        print("\n[Failed] You couldn't break the AES encryption! Try again.")
        return  # หยุดเกมหากภารกิจที่ 3 ไม่สำเร็จ
    
    print("=" * 60)
    print()
    time.sleep(2)
    loading_animation()
    print()
    
    # ตอนจบ
    print("\n[Conclusion] The hack is complete!")
    print("Congratulations! You successfully unlocked the banking system and stole the millions!")
    print("Your name will be etched in the legends of the cyber underground... The SR2N!")
    print("\n[Crypto Heist: Mission Accomplished]")
    print()
    print("=" * 60)

# เรียกใช้งานฟังก์ชัน
if __name__ == "__main__":
    play_game()

