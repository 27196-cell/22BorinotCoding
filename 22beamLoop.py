import random
number = random.randint(1, 101)
guess = int(input("ใส่คำตอบ(1-100): "))

print(guess)
while number != guess:

    if guess < number:
        print("น้อยเกินไป")
        guess = int(input("ใส่คำตอบอีกครั้ง: "))
    elif guess > number:
        print("มากเกินไป")
        guess = int(input("ใส่คำตอบอีกครั้ง: "))
    else:
        break
print("คุณทายถูก!")
print("คุณทายไป", guess)