from account import Account

class SavingsAccount(Account):

    def __init__(self, balance: float, annual_interest_rate: float):
        super().__init__(balance, annual_interest_rate)
        self._ALLOWED_BALANCE = 25.0
        self.status = self._is_active()

    def deposit(self, amount: float):
        self._validate_amount(amount)
        if not self.status and amount > self._ALLOWED_BALANCE :
            self.status = True
            super().deposit(amount)

    def withdraw(self, amount: float):
        if self.status:
            super().withdraw(amount)

    def _is_active(self):
        status : bool = True
        if self.balance < self._ALLOWED_BALANCE: 
            status = False

        return status

    