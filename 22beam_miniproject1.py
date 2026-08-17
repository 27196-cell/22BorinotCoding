from datetime import datetime
import calendar
import time
import winsound

year = datetime.now().year
month = int(input("ระบุเดือน (1-12): "))
target_time = datetime(year, month, (int(input("ระบุวัน (1-31): "))))

print("       วันที่กำหนดส่งงาน")
print(" Mo  Tu  We  Th  Fr  Sa  Su")

cal = calendar.monthcalendar(year, month)
for week in cal:
    for day in week:
        if day == 0:
            print("    ", end="")
        elif day == target_time:
            print(f"[{day:2}]", end="")
        else:
            print(f" {day:2} ", end="")
    print()

remaining = (target_time - datetime.now()).days

print("เหลือเวลาอีก:", remaining ,"วัน")
print()

print("กำลังรอกำหนด...")
while True:
    now = datetime.now()
    if now >= target_time:
        print("ครบกำหนดแล้ว")
        winsound.Beep(700, 2000)
        break
    time.sleep(60)