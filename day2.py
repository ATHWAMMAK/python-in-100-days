print("--- M-Pesa Fight Pass ---")
balance = int(input("Enter your balance: "))
price = 300

if balance >= price:
    remaining_balance = balance - price
    print(f"Success! Paid {price}. Remaining: {remaining_balance} KES")
    print(f"Enjoy your M-Pesa Fight Pass!")

else:
    needed = price - balance
    print(f"Failed! You need {needed} KES more to purchase the M-Pesa Fight Pass.")

print("\n--- KCSE Grader ---")
marks = int(input("Enter your marks(0-100): "))

if marks >= 80:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "D - Try again"
    
    print(f"Your grade is: {grade}")
    