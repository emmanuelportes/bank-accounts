import uuid

class Account:

    def __init__(self):
        self._id = self._generate_id()
        self._balance = 0.0

    # method to deposit money to the account
    def deposit(self, amount: float) :
        if (type(amount) is not float) and amount <= 0.0 :
            raise ValueError("invalid ammount provided")
        
        self._balance = self._balance + amount
                
    # method to withdraw money from the account

    # method to transfer to the account
    # method to show balance
    @property
    def balance(self) -> float:
        return self._balance
    
    @property
    def id(self) -> str :
        return self._id
        
    def _generate_id(self) -> str:
        return uuid.uuid4()


acc = Account()

acc.deposit(500.0)
print(acc.balance)

