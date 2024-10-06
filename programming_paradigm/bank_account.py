class BankAccount:
  def __init__(self, initial_balance=0):
    self.account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.account_balance += amount
      print(f"Deposited ${amount:.2f}. New balance: ${self.account_balance:.2f}")
    else:
      print("Invalid deposit amount. Please enter a positive value.")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.account_balance:
      self.account_balance -= amount
      print(f"Withdrew ${amount:.2f}. New balance: ${self.account_balance:.2f}")
      return True
    else:
      print(f"Insufficient funds. Balance: ${self.account_balance:.2f}")
      return False

  def display_balance(self):
    print(f"Current balance: ${self.account_balance:.2f}")
