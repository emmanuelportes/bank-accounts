import uuid
from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, balance: float, annual_interest_rate: float) :
        self.balance = balance
        self._number_of_withdrawls = 0
        self._id = self._generate_id()
        self._number_of_monthly_deposits = 0
        self._annual_interest_rate = annual_interest_rate

    @abstractmethod
    def deposit(self, amount: float) :
        pass

    @abstractmethod    
    def withdraw(self, amount: float) :
        pass

    @property
    def id(self) -> str :
        return self._id

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

    @property
    def annual_interest_rate(self):
        return self._annual_interest_rate
           
    def _validate_amount(self, amount: float) :
           
           if not isinstance(amount, float):
               raise TypeError("invalid value type provided")
           
           if amount <= 0.0 :
               raise ValueError("invalid amount provided")
    
    def _generate_id(self) -> str:
        return uuid.uuid4()
