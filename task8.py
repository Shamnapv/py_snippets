class Money:
    def __init__(self,amount):
        self.amount=amount
    def __add__(self,other):
        return Money(self.amount+other.amount)
    def __sub__(self,other):
        return Money(self.amount-other.amount)
    def __mul__(self,factor):
        return Money(self.amount*factor)
    def __str__(self):
        return f"{self.amount}"
    
class item:
    def __init__(self,price):
        self.price=price
    def __mul__(self,quantity):
        return Money(self.price*quantity)
    def __str__(self):
        return f"Item price: {self.price}"
    
wallet=Money(1000)
gift=Money(250)
Item=item(100)
print("wallet",wallet)
print("gift",gift)
print("Item",Item)

print("operations")
print("Total Money (Wallet + Gift):",wallet+gift)
print("Remaining Money (Wallet - Gift):",wallet-gift)
print("Double the gift value:",gift*2)

print("Cost of 5 items:",Item *5)

"""output:
(base) PS C:\Users\shaim\Desktop\pythonlab> python task8.py
wallet 1000
gift 250
Item Item price: 100
operations
Total Money (Wallet + Gift): 1250
Remaining Money (Wallet - Gift): 750
Double the gift value: 500
Cost of 5 items: 500
"""