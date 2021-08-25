class Atm():
    def __init__(self, atmCardNumber , pinNumber):
        self.atmCardNumber = atmCardNumber
        self.pinNumber = pinNumber

    def cashWithdrawl(self):
        return "this method withdrawed our cash"

    def balancEnquiry(self):
        return 'this method warned you about your bank balance'


bankAccount1 = Atm(342234334514 , 6451)
print(bankAccount1.pinNumber)
print(bankAccount1.atmCardNumber)
print(bankAccount1.cashWithdrawl())
print(bankAccount1.balancEnquiry())