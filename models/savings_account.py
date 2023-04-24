from account import Account

class SavingsAccount(Account):

    def __init__(self, balance: float, annual_interest_rate: float):
        super().__init__(balance, annual_interest_rate)
        self._ALLOWED_BALANCE = 25.0
        self.status = True

    def deposit(self, amount: float):
        super()._validate_amount(amount)
        if not self._is_active() and amount > self._ALLOWED_BALANCE :
            self.status = True
            super().deposit(amount)

    def withdraw(self, amount: float):
        if self._is_active():
            super().withdraw(amount)

    def _is_active(self):
        if self.balance < self._ALLOWED_BALANCE: 
            self.status = False
        return self.status

    