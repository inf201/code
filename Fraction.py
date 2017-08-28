def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

     def getNum(self):
     	return self.num 

     def getDen(self):
     	return self.den


     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum
     
     def __sub__(self, subfrac):
         newnum = self.num*subfrac.den - self.den*subfrac.num 
         newden = self.den * subfrac.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)
     
     def __mul__ (self,other):
         newnum = self.num * other.num
         newden = self.den * other.den 
         common = gcd(newnum,newden)
         return Fraction (newnum//common,newden//common)
     
     def __div__(self, other):
         newnum = self.num * other.den
         newden = self.den * other.num
         common = gcd(newnum,newden)
         return Fraction(newnum//common, newden//common)

         
         
x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)
print(x-y)
print(x*y)
print(x/y)
print (x.getNum( ))
print (x.getDen( ))
