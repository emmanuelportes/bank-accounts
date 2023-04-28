from models.savings_account import SavingsAccount

def main():
    
    sacc = SavingsAccount(600.0, 1.2)
    sacc.deposit(300.0)

    print(sacc.balance)
    sacc.withdraw(600)
    print(sacc.balance)

if __name__ == "__main__":
    main()

