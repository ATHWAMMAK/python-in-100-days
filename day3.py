print("--- Shadow Boxing Rounds ---")
for round in range(1, 6):
    print(f"Round {round}: 50 punches!")

    total = 0
    for punch in range(1, 51):
        total += 50
    print(f"Total punches in Round {round}: {total}")

print("\n--- Top-up Loop ---")
balance = int(input("Enter your balance: "))
price = 300

while balance < price:
    needed = price - balance
    print(f"Failed! You need {needed} KES more to purchase the M-Pesa Fight Pass.")
    top_up = int(input("Enter amount to top-up: "))
    balance += top_up
    print(f"New balance: {balance} KES")

    print(f"Done! You have {balance} - Fight Pass granted!")

    