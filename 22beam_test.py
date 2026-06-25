print("คำนวณ BMI\n")

Kg = int(input("ระบุน้ำหนัก: "))
M = float(input("ระบุส่วนสูง(เมตร): "))
proc = Kg / (M * M)
BMI = round(proc, 1)

print("ค่า BMI:",BMI)
if BMI < 18.5:
    print("อยู่ในเกณฑ์ น้ำหนักน้อย")
elif BMI <= 22.9:
    print("อยู่ในเกณฑ์ ปกติ")
elif BMI <= 24.9:
    print("อยู่ในเกณฑ์ น้ำหนักเกิน")
else:
    print("อยู่ในเกณฑ์\nอ้วน")
