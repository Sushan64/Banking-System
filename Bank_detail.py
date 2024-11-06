class Bank:
  def __init__(self, name, type, amount):
    self.name = name
    self.type = type
    self.amount = amount

  #to find bank details
  def show_bank(self):
    print("Account Name: ", self.name)
    print("Account Type: ", self.type)
    print(f"Balance: Rs. {self.amount:.2f}")

  #to deposit amount
  def deposit(self, amount):
    self.amount += amount
    print(f"Successfully Deposited Rs. {amount}")

  #to withdraw amount
  def withdraw(self, amount):
    if self.amount >= amount:
      self.amount -= amount
      print("Successfully Withdrawn Rs.", amount)
    else:
      print("Insufficient Balance")  

  #to show current balance
  def show_balance(self):
    return self.amount
