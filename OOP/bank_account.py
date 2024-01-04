class BalanceException(Exception):
     pass

class BankAccount:
    def __init__(self,initialAmount: float, accName: str):
        self.balance=initialAmount
        self._name=accName
    
    def __str__(self):
        return f"""
        Account {self._name} created.
        Balance = ${round(self.balance,2)}"""
    
    def getBalance(self):
        return f"""Account {self._name} :${round(self.balance,2)}"""
        
    
    def deposit(self, value):
       
            assert type(value)==float or type(value)==int, "Deposit needs to be a number!"
            self.balance+=value
            return f"Deposit of ${value} completed"
    
    def viableTransaction(self,amount):
         if self.balance>=amount:
              return
         else:
              raise BalanceException(f"""Sorry, {self._name}'s Account Balance only have balance of $${round(self.balance,2)}""")
         
    def withdraw(self,amount):
        try:
              self.viableTransaction(amount)
              self.balance-=amount
              print( "Withdraw complete")
              return self.getBalance()  
        except BalanceException as Error:
             print(f"Withdraw interuppted :\n {Error}")


    def transfer(self,amount,account):
        try:
              print("******Beginning Transfer...*******")
              self.viableTransaction(amount)
              self.withdraw(amount)
              account.deposit(amount)
              print("******Transfer Complete******")
        except BalanceException as Error:
             print(f"Transfor interuppted :\n {Error}")
    

class IntrestRewardsAcct(BankAccount):
        
        def __init__(self, initialAmount: float, accName: str):
             super().__init__(initialAmount, accName)
        
             
        
        def deposit(self, value: float):
            print("Depositing Into InterestRewardsAcct...")
            self.balance =self.balance +(value* 1.05)
           
            return f"Deposit of ${value} completed with interest. New balance: ${round(self.balance, 2)}"                         
        
class SavingsAcct(IntrestRewardsAcct):
     def __init__(self, initialAmount: float, accName: str):
          super().__init__(initialAmount, accName)
          self.fee=5
     def withdraw(self, amount):
          try:
               self.viableTransaction(amount+self.fee)
               self.balance=self.balance-(amount+self.fee)
               print("\n Withdraw Complete")
               self.getBalance()
          except(BalanceException) as Error:
               print(f'\n Withdraw interuppted: {Error}')
            
        
        



                            
        
            
