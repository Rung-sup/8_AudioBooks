import os
import subprocess

# ==========================================
# แก้ไขลิงก์เพลย์ลิสต์ตรงนี้
# ==========================================
PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLfhTfuFWys39qsT-e_iuGRL-MHm0g0RRm"
OUTPUT_FILE = "links.txt"
# ==========================================

def extract_playlist():
    print(f"กำลังดึงข้อมูลจากเพลย์ลิสต์... กรุณารอครู่หนึ่ง")
    
    cmd = [
        'yt-dlp', 
        '--flat-playlist', 
        '--print', '%(title)s\n%(url)s', 
        PLAYLIST_URL
    ]
    
    try:
        # ดึงข้อมูลดิบออกมาก่อน
        result = subprocess.run(cmd, capture_output=True)
        raw_data = result.stdout

        # พยายามถอดรหัส (ลอง UTF-8 ก่อน ถ้าไม่ได้ให้ใช้ CP874 ของ Windows Thai)
        try:
            decoded_text = raw_data.decode('utf-8')
        except UnicodeDecodeError:
            decoded_text = raw_data.decode('cp874', errors='replace')

        if decoded_text.strip():
            # บันทึกเป็น UTF-8 เพื่อให้ Super_Master_Workflow อ่านได้ถูกต้อง
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                f.write(decoded_text.strip())
            
            count = len(decoded_text.strip().split('\n')) // 2
            print(f"✨ สำเร็จ! ดึงข้อมูลภาษาไทยมาได้ {count} ตอน")
            print(f"📂 ตรวจสอบไฟล์ได้ที่: {os.path.abspath(OUTPUT_FILE)}")
        else:
            print("❌ ไม่พบข้อมูลในเพลย์ลิสต์")

    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {str(e)}")

if __name__ == "__main__":
    extract_playlist()