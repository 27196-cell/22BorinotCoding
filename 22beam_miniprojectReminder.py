from datetime import datetime
import calendar

year = datetime.now().year
month = int(input("ระบุเดือน (1-12): "))
target_day = int(input("ระบุวัน (1-31): "))

print(" Mo  Tu  We  Th  Fr  Sa  Su")

cal = calendar.monthcalendar(year, month)

for week in cal:
    for day in week:
        if day == 0:
            print("    ", end="")
        elif day == target_day:
            print(f"[{day:2}]", end="")
        else:
            print(f" {day:2} ", end="")
    print()