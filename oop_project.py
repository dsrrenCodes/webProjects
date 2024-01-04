from bank_account import BankAccount, IntrestRewardsAcct, SavingsAcct
Sara=BankAccount(1000,"Sara")
Blaze=SavingsAcct(1000,"Blaze")
(Blaze.getBalance())
print(Blaze.deposit(100))

Blaze.transfer(10000,Sara)
