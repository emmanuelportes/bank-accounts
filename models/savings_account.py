from models.account import Account

class SavingsAccount(Account):

    def __init__(self, balance: float, annual_interest_rate: float):
        super().__init__(balance, annual_interest_rate)
        self._ALLOWED_BALANCE = 25.0
        self.status = True

    def deposit(self, amount: float):
        super()._validate_amount(amount)
        if amount > self._ALLOWED_BALANCE :
            if not self._is_active():
                self._change_status()
            super().deposit(amount)

    def withdraw(self, amount: float):
        if self._is_active():
            super().withdraw(amount)
            return
        
        print("currently, this account is inactive")

    def _monthly_process(self):
        if self.number_of_withdrawals > 4:
            self._service_charges = self.number_of_withdrawals - 4
            super()._monthly_process()

            if self._is_active() :
                self._change_status()

    def _change_status(self):
        if self.balance < self._ALLOWED_BALANCE: 
            self.status = False
        else:
            self.status = True

    def _is_active(self) -> bool:
        return self.status