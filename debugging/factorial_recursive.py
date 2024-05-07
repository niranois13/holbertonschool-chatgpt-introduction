class Checkbook:
	"""
	A class to represent a simple checkbook.

	Attributes:
		balance (float): The current balance in the checkbook.
	"""

	def __init__(self):
		"""
		Initializes a new Checkbook object with a balance of 0.0.
		"""
		self.balance = 0.0

	def deposit(self, amount):
		"""
		Deposits a specified amount into the checkbook.

		Args:
			amount (float): The amount to be deposited.

		Returns:
			None
		"""
		try:
			amount = float(amount)
		except ValueError:
			print("Invalid input. Please enter a valid numeric amount.")
			return

		self.balance += amount
		print("Deposited ${:.2f}".format(amount))
		print("Current Balance: ${:.2f}".format(self.balance))

	def withdraw(self, amount):
		"""
		Withdraws a specified amount from the checkbook, if sufficient funds are available.

		Args:
			amount (float): The amount to be withdrawn.

		Returns:
			None
		"""
		try:
			amount = float(amount)
		except ValueError:
			print("Invalid input. Please enter a valid numeric amount.")
			return

		if amount > self.balance:
			print("Insufficient funds to complete the withdrawal.")
		else:
			self.balance -= amount
			print("Withdrew ${:.2f}".format(amount))
			print("Current Balance: ${:.2f}".format(self.balance))

	def get_balance(self):
		"""
		Displays the current balance of the checkbook.

		Returns:
			None
		"""
		print("Current Balance: ${:.2f}".format(self.balance))

def main():
	"""
	The main function to interact with the Checkbook class.

	Returns:
		None
	"""
	cb = Checkbook()
	while True:
		action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
		if action.lower() == 'exit':
			break
		elif action.lower() == 'deposit':
			amount = input("Enter the amount to deposit: $")
			cb.deposit(amount)
		elif action.lower() == 'withdraw':
			amount = input("Enter the amount to withdraw: $")
			cb.withdraw(amount)
		elif action.lower() == 'balance':
			cb.get_balance()
		else:
			print("Invalid command. Please try again.")

if __name__ == "__main__":
	main()