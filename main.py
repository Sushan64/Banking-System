#banking system

#import Class from external file, Bank_detail.py file.
import Bank_detail


#program to open bank account
try:
  print("———Open Your Bank———")
  name = input("Your Name: ")
  type = input("Account Type: ")
  balance = int(input("Your Initial deposit: "))
  print("———Successfully Created Your Bank Account———")

except ValueError:
  print("Couldn't Open Your Bank Account ")
  

#adding Class Bank details into a variable b
b = Bank_detail.Bank(name, type, balance)

print("—————Your Bank Details—————")
b.show_bank()

#while True to always run to_deposite variable
while True:
  to_deposite = input("Do You Want to Deposit or Withdraw (D/W): " ).upper()

  #checking input
  if to_deposite == "D":
    dep_amount = int(input("Your Account to Deposit: "))
    b.deposit(dep_amount)
    print("———Successfully Deposited———")
  elif to_deposite == "W":
    draw_amount = int(input("Your Amount to Withdraw: "))
    b.withdraw(draw_amount)
    print("———Successfully Withdraw———")
  else:
    print("Please Enter W or D only!")
  
  
  print(f"Your New balance is Rs.{b.show_balance()}")

