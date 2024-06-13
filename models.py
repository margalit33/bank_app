class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
    -----------
    account_number : int
        The account number of the bank account.
    name : str
        The name of the account holder.
    balance : float
        The balance of the bank account.
    """

    def __init__(self, account_number, name, balance):
        """
        Constructs all the necessary attributes for the bank account object.

        Parameters:
        ----------
        account_number : int
            The account number of the bank account.
        name : str
            The name of the account holder.
        balance : float
            The balance of the bank account.
        """
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __repr__(self):
        """
        Returns a string representation of the bank account.
        """
        return f"Account({self.account_number}, {self.name}, {self.balance})"


class Bank:
    """
    A class to represent a bank.

    Attributes:
    -----------
    accounts : list
        The list of bank accounts in the bank.
    next_account_number : int
        The next account number to be assigned to a new account.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the bank object.
        """
        self.accounts = []
        self.next_account_number = 1

    def create_account(self, name, initial_balance):
        """
        Creates a new bank account and adds it to the accounts list.

        Parameters:
        ----------
        name : str
            The name of the account holder.
        initial_balance : float
            The initial balance of the new bank account.
        """
        account = BankAccount(self.next_account_number, name, initial_balance)
        self.accounts.append(account)
        self.next_account_number += 1

    def get_all_accounts(self):
        """
        Returns a list of all bank accounts.
        """
        return self.accounts
