print("โปรแกรมคำนวณคะแนน")

Eng = int(input("ระบุคะแนนวิชาภาษาอังกฤษ: "))
Math = int(input("ระบุคะแนนวิชาคณิตศาสตร์: "))
Chemistry = int(input("ระบุคะแนนวิชาเคมี: "))

total_point = Eng + Math + Chemistry
average = int(total_point /3)

print("คะแนนรวม:",total_point)
print("คะแนนเฉลี่ย:", average)
if average < 60:
    print("ควรปรับปรุง")
elif average < 80:
    print("ผ่าน")
else:
    print("ดีเยี่ยม")
print("made by Borinot Maiaiem Beam No.22")