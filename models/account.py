import uuid
from abc import ABC

class Account(ABC):

    def __init__(self, balance: float, annual_interest_rate: float) :
        self.balance = balance
        self.number_of_withdrawls = 0
        self._id = self._generate_id()
        self.number_of_monthly_deposits = 0
        self._annual_interest_rate = annual_interest_rate

    def deposit(self, amount: float) :

        self._validate_amount(amount)
        self.balance = self.balance + amount
        self.number_of_monthly_deposits += 1

    def withdraw(self, amount: float) :

        self._validate_amount(amount)
        remaining_balance = self.balance - amount

        if remaining_balance >= 0 :
            self.balance -= self.balance - amount
            self.number_of_withdrawls += 1

    def calculate_interest(self) :
        pass

    def monthly_process(self) :
        pass

    @property
    def id(self) -> str :
        return self._id
    
    @property
    def annual_interest_rate(self):
        return self._annual_interest_rate

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
           
           if not isinstance(amount, float):
               raise TypeError("invalid value type provided")
           
           if amount <= 0.0 :
               raise ValueError("invalid amount provided")
    
    def _generate_id(self) -> str:
        return uuid.uuid4()
