class atm():
    def __init__(self,pin,number,balance):
        self.pin = pin
        self.number = number
        self.balance = balance
    def signin1(self):
        pinone = '7123'
        number2 = '121212'
        # print(self.balance)
        if self.pin == pinone and self.number == number2:
            print(self.balance)
balance1 = 5000

tellcardnumber = input("Enter you cardnumberhere: ")

tellpin = input("Enter you pin here: ")

start = atm(tellpin,tellcardnumber,balance1)

start.signin1()


