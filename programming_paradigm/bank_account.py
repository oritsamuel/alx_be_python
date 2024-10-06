class BankAccount:
  """
  A class representing a bank account.
  """

  def __init__(self, initial_balance=0):
    """
    Initializes a new bank account with an optional initial balance.

    Args:
      initial_balance (float, optional): The initial balance of the account. Defaults to 0.
    """
    self.account_balance = initial_balance

  def deposit(self, amount):
    """
    Deposits a specified amount into the account.

    Args:
      amount (float): The amount to deposit.

    Returns:
      None
    """
    if amount > 0:
      self.account_balance += amount
      print(f"Deposited ${amount:.2f}. New balance: ${self.account_balance:.2f}")
    else:
      print("Invalid deposit amount. Please enter a positive value.")

  def withdraw(self, amount):
    """
    Withdraws a specified amount from the account, if sufficient funds are available.

    Args:
      amount (float): The amount to withdraw.

    Returns:
      bool: True if the withdrawal was successful, False otherwise.
    """
    if amount > 0 and amount <= self.account_balance:
      self.account_balance -= amount
      print(f"Withdrew ${amount:.2f}. New balance: ${self.account_balance:.2f}")
      return True
    else:
      print(f"Insufficient funds. Balance: ${self.account_balance:.2f}")
      return False

  def display_balance(self):
    """
    Prints the current balance in a user-friendly format.

    Returns:
      None
    """
    print(f"Current balance: ${self.account_balance:.2f}")
