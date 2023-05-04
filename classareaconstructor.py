class Sha:
    def _init_(self,leng,bre):
        self.l=leng
        self.b=bre
        
    def area(self):
        self.a=self.l*self.b
        print("Area of the Rectangle:",self.a)
        

leng=int(input("Enter the length of the Rectangle:"))
bre=int(input("Enter the breadth of the Rectangle:"))
s=Sha(leng,bre)
s.area()
