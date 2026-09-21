name = input("Name: ")
balance = int(input("Balance: "))
city = input("City: ")

print("\n--- Receipt ---")
print(f"Hello {name} from {city}!")
print(f"Your balance: KES {balance}")

transaction = int(input("Withdrawal: "))
new_balance = balance - transaction
print(f"After sending KES {transaction}, you will now have KES {new_balance}")
