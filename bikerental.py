# class for setup 
class bikeshop:
    def __init__(self, stock):
        self.stock=stock
    def displaybike(self):
        print("Total bike ", self.stock)
    def rentForBike(self,q):
        if q<=0:
            print("enter the positive number ")
        elif q>self.stock:
            print("enter the value(less than 100)")
        else:
            self.stock=self.stock - q
            print("total prices", q*100)
            print("total bike",self.stock)

while True:
    obj = bikeshop(100)
    uc=int(input('''
1. Display stock
2. Rent a bike
3. Exit 
'''))
    
    if uc==1:
        obj.displaybike()
    
    elif uc==2:
        n=int(input("enter the qun......."))
        obj.rentForBike(n)
    else:
        break 

    