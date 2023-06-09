import uuid
from abc import ABC

class Account(ABC):

    def __init__(self, balance: float, annual_interest_rate: float) :
        self.balance = self._check_opening_balance(balance)
        self.number_of_withdrawals = 0
        self._id = self._generate_id()
        self._service_charges = 0
        self.number_of_monthly_deposits = 0
        self._ANNUAL_INTEREST_RATE = annual_interest_rate
        self._ZERO = 0

    def deposit(self, amount: float) :
        self._validate_amount(amount)
        self.balance = self.balance + amount
        self.number_of_monthly_deposits += 1

    def withdraw(self, amount: float) :
        self._validate_amount(amount)
        remaining_balance = self.balance - amount

        if remaining_balance > self._ZERO :
            self.balance -= amount
            self.number_of_withdrawals += 1

    def _calculate_interest(self) :
        monthly_interest_rate = (self._ANNUAL_INTEREST_RATE / 12)
        monthly_interest = self.balance * monthly_interest_rate
        self.balance += monthly_interest

    def _monthly_process(self) :
        self.balance -= self._service_charges
        self.number_of_monthly_deposits = 0
        self.number_of_withdrawals = 0
        self._calculate_interest()

    def _check_opening_balance(self, amount:float):
        INITIAL_AMOUNT: float = 500.0
        if amount >= INITIAL_AMOUNT:
            return amount
        
        raise ValueError(f"opening deposit must be above 500.0. currently: {amount}")

    @property
    def id(self) -> str :
        return self._id
    
    @property
    def annual_interest_rate(self):
        return self._ANNUAL_INTEREST_RATE

    @property
    def balance(self) -> float :
        return self._balance
    
    @balance.setter
    def balance( self, balance: float) :
        if not isinstance(balance, float) :
            raise TypeError("invalid value type provided") 
        
        if balance <= 0 :
            raise ValueError("invalid balance provided")
        
        self._balance = balance

    def _validate_amount(self, amount: float) : 
        if isinstance(amount, float) or isinstance(amount, int):
            return
        elif amount <= 0.0 :
            raise ValueError("invalid amount provided")
        else:
            raise TypeError("invalid value type provided")
           
    def _generate_id(self) -> str:
        return uuid.uuid4()
