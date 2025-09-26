class bikeshop:
    #stock=100
    def __init__(self,stock):
        self.stock=stock
        print(self.stock)
    def displaybike(self):
        print("total bike",self.stock)
    def rentforbike(self,q):
        if q<=0:
            print("enter the positive value or greater than  the zero ")
        elif q>self.stock:
            print("enter the value (less the stock)")
        else:
            self.stock=self.stock=q
            print("total prices ",q*100) 
            print("total bikes",self.stock)
while True:
    obj =bikeshop(100)
    uc=  int(input(
            '''1 display stock
            2 rent a bike
            3 exit ''' ))
    if uc ==1:
        obj.displaybike()
    elif uc ==2:
        n=int(input("enter qty"))
        obj.rentforbike(n)
    else:
        break
            

