name = input("Enter your name: ")
balance = int(input("Enter your balance: "))
city = input("Enter your city: ")

print("\n--- Receipt ---")
print(f"Hello {name} from {city}!")
print(f"Your balance: KES {balance}")

transaction = int(input("Enter amount to send: "))
new_balance = balance - transaction
print(f"After sending KES {transaction}, you will now have KES {new_balance}")
