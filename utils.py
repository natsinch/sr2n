import matplotlib.pyplot as plt
import time
import hashlib

def show_image(image_path):
    """
    แสดงภาพจากไฟล์ที่กำหนด
    """
    try:
        img = plt.imread(image_path)
        plt.imshow(img)
        plt.axis("off")
        plt.show()
    except FileNotFoundError:
        print(f"ไม่พบไฟล์ภาพ: {image_path}")

def display_hacking_graphics():
    """
    แสดงกราฟฟิกการแฮ็กแบบจำลอง
    """
    for i in range(5):
        print(f"[Hacking data...  {i * 20}%]")
        time.sleep(0.5)
    print("[Hack successful!]")

import time

def loading_animation(repeat_count=10):
    loading_symbols = ['|', '/', '-', '\\']
    for _ in range(repeat_count):  # จำนวนวนรอบตามที่ต้องการ
        for symbol in loading_symbols:
            print(f"\rLoading {symbol}", end='', flush=True)
            time.sleep(0.2)  # กำหนดเวลาหมุนแต่ละครั้ง
    print("\rLoading complete!")  # พิมพ์ข้อความเมื่อโหลดเสร็จ

    
def print_story():
    story = """
    Welcome to Crypto Heist!

    You are **The SR2N**, a high-level hacker from the underground world...
    No one knows you in the online world, but your name is well-known among those who have the power to break into the most secure systems in the digital world.

    Today, your mission has shifted from typical system hacks. This is about infiltrating the **most highly secured digital banking system** ever created. A system built by organizations with top-tier technology from governments and secret agencies worldwide.

    You’ve been ordered by a secret group known as **The P**, who will have you steal millions of dollars from hidden accounts within this system. But it’s not as easy as it sounds. This system is protected by **AES**, **RSA**, and **SHA-256** encryption, presenting a serious challenge. You’ll need to use your best hacking techniques to break through.

    **Your actions must be silent and swift**—there’s no time for mistakes. If you break the encryption incorrectly, the system will immediately activate its defense mechanisms, and everything will collapse around you.

    This job isn’t just about money; it’s a battle to prove legendary skills!
    """
    print(story)
