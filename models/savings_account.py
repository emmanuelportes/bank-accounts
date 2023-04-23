from account import Account

class SavingsAccount(Account):

    def __init__(self, balance: float, annual_interest_rate: float):
        super().__init__(balance, annual_interest_rate)
        self._ALLOWED_BALANCE = 25.0
        self.status = self._is_account_active()

    def deposit(self, amount: float):
        pass

    def withdraw(self, amount: float):
        pass

    def _is_account_active(self):
        status : bool = True
        
        if self.balance < self._ALLOWED_BALANCE: 
            status = False

        return status

    