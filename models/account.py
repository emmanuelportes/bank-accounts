import uuid

class Account:

    def __init__(self):
        self._id = self._generate_id()
        self._balance = 0.0

    def deposit(self, amount: float) :
        self._validate_amount(amount)     
        self.balance += amount
                
    def withdraw(self, amount: float) :
        self._validate_amount(amount)
        remaining = self.balance - amount

        if remaining > 0:
            self.balance = remaining


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
       

    def _validate_amount(self, amount: float) :
           
           if not isinstance(amount, float):
               raise TypeError("invalid value type provided")
           
           if amount <= 0.0 :
               raise ValueError("invalid amount provided")
    
    def _generate_id(self) -> str:
        return uuid.uuid4()


acc = Account()

acc.deposit(100.0)
print(acc.balance)
print(acc.id)
