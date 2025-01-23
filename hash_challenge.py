import hashlib
from utils import show_image
from utils import display_hacking_graphics

# ข้อความที่ถูกแฮช
hashed_password = hashlib.sha256("CPESUT".encode()).hexdigest()

def hash_task():
    print("-" * 60)
    print("Hint: Find the hidden message in the image")
    show_image("images/hint3.png")
    print("You need to enter the password to proceed to the next mission!!")
    
    # รับค่าแฮชจากผู้ใช้
    while True:
        user_hash = input("Enter the hash you think is the correct answer: ").strip()
        if user_hash == hashed_password:
            display_hacking_graphics()
            print("The hash is correct! Proceeding to the next mission.")
            return True
        else:
            print("The hash is incorrect! Try again.")

# เรียกใช้งานฟังก์ชัน
#hash_task()
