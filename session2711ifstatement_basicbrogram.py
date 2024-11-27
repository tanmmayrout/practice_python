#Basic program for if statement practice

median_price= 1000000

print("The minimum price to buy a house is ",median_price)
bank_balance= int(input("Enter the balance of your bank account" ))

print(type(bank_balance))
print("Your bank balance is",bank_balance)

if bank_balance >= median_price:
    has_good_credit = True
    print("You have good credit")
else:
    has_good_credit = False
    print("You dont have good credit")


if has_good_credit:
    down_payment = 0.1*bank_balance
else:
    down_payment = 0.2*bank_balance
print(f"Down Payment: {down_payment}")







