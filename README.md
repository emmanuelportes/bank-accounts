# Bank Accounts

This project simulates basic aspects of some of the accounts provided by banks. Currently, just the base account and it's derived savings account are available.

## Class design paramenters

Design an abstract class named BankAccount to hold the following data for a bank account:

Balance  - private
Number of deposits this month
Number of withdrawals
Annual interest rate

The class should have the following methods:

Constructor: the constructor should accepts an arguments for the balance and annual interest rate

Deposit: A method that accepts an argument for the amount of the deposit. The method should add the argument to the account balance. It should also increment the variable holding the number of deposits.

Withdraw: A method that accepts an argument for the amount of the withdrawal. The method should subtract the argument from the balance. It should also increment the variable holding the number of withdrawals.

calcInterest: A method that updates the balance by calculating the monthly interest earned by the account and adding this interest to the balance. This is performed by the following formulas:

Monthly interest rate=(annual interest rate/12)
Monthly interst=balance*monthly interest rate  
Balance=balance + monthly interest

monthlyProcess: A method that subtracts the monthly service charges from the balance, calls the calcInterest method and then sets the variables that hold the number of withdrawals, number of deposits, and monthly service charges to zero.

Next design a SavingsAccount class that extends the BankAccount class.

The SavingAccount class should have a status field to represent an active or inactive account. If the balance of a savings account falls below $25 it becomes inactive. ( the status field could be a Boolean variable) No more withdrawals may be made until the balance is raised above $25 at which time the account becomes active again.

The savings account class should have the following methods:

withdraw: A method that determines whether the account is inactive before a withdrawal is made. (No withdrawal will be allowed if the account is not active).  A withdrawal is then made by calling the superclass version of the method.

deposit: A method that determines whether the account is inactive before a deposit is made. If the account is inactive and the deposit brings the balance above $25, the account becomes active again. A deposit is then made by calling the superclass version of the method.

monthlyProcess: Before the superclass method is called, this method checks the number of withdrawals. If the number of withdrawals for the month is more than 4, a service charge of $1 for each withdrawal above 4 is added to the superclass field that holds the monthly service charges. (Don’t forget to check the account balance after the service charge is taken. If the balance falls below $25 the account becomes inactive.)  

## Current project structure

- models/
    - account.py
    - savings-account.py
-   main.py