
# bank account management sytem

class Bankaccount:
    account_used=0
    def __init__(self,account_number,account_holder,balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.__balance=balance
        Bankaccount.account_used+=1

    def deposit(self,amount):
        
        self.account_holder
        self.account_number
        self.__balance
        self.amount=amount
        return f"your desosit amounit is :{amount},and your total balance is :{self.__balance+amount}"
    

    def get__balance(self):
        return self.__balance
    
    def withdraw(self,withdraw_amount):
        self.withdraw_amount=withdraw_amount
        self.__balance
        if withdraw_amount>self.__balance:
            print("insufficent balance please check your balance ")
        else:
            print(f"your withdraw amount is:{withdraw_amount},and your available balanve is:{self.__balance-withdraw_amount}")

    def display_balance(self):
        self.__balance
        return f"you have {self.__balance} rupees in your account "
    


class SavingAccount(Bankaccount):
    def add_intrest(self):
        intrest=self.__balance*0.005
        self.__balance+=intrest
        return f"your bankbalance after adding 0.5% intrest is :{self.__balance}"

        # return f"your account balance:{self.balance},and after adding intrest your balance is ({self.balance*0.005 + self.balance})"



class CurrentAccount(Bankaccount):
    def overdraft_limit(self,overdraft):
        self.__balance
        self.overdraft=overdraft
        if overdraft>(self.__balance+5000):
            print(f"insufficent overdraft , you can only overdraft upto {self.__balance+5000}")
        else:
            print("withdraw sucessful ")



my_depo=Bankaccount(9229586269,"vivek",5600)
print(my_depo.deposit(500))
# print(my_depo.withdraw_amount())
print(my_depo.deposit(5000))
print(my_depo.withdraw(1000))

isinstance(my_depo,Bankaccount)

print(isinstance(my_depo,Bankaccount))

sav_acc=SavingAccount(9229586269,"viveksah",500000)



over_draff=CurrentAccount(9229586269,"viveksah",5000)
# print(over_draff.overdraft_limit(3999))


print(my_depo.get__balance())
print(my_depo.account_used)

