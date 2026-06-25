Kg = int(input("ระบุน้ำหนัก: "))
M = float(input("ระบุส่วนสูง(เมตร): "))
proc = Kg / (M * M)
BMI = round(proc, 1)

print("ค่า BMI:",BMI)
if BMI < 18.5:
    print("น้ำหนักน้อย")
elif BMI <= 22.9:
    print("ปกติ")
elif BMI <= 24.9:
    print("น้ำหนักเกิน")
else:
    print("อ้วน")