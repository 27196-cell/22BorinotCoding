print("\nโปรแกรมคำนวณสูตรคูณ v.2\n")

n = int(input("ใส่ตัวเลขแม่เริ่มต้น: "))
n2 = int(input("ใส่ตัวเลขแม่สิ้นสุด: "))

for m in range(n, n2 + 1):
    print("\nแม่",m)
    for i in range(1, 13):
        print(m, "x", i, "=", m * i)
print("\nบริณต ใหม่เอี่ยม")