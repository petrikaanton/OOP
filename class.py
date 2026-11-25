class Ratio:
    def __init__(self,num1,num2):
        self.nominator = num1
        self.denominator = num2

    def simply(self):
        temp1 = self.nominator
        temp2 = self.denominator
        while temp1 != temp2:
            if temp1 > temp2:
                temp1 = temp1 - temp2
            else:
                temp2 = temp2 - temp1

        if temp1 != 1:
            self.nominator = self.nominator // temp1
            self.denominator = self.denominator // temp1

    def __str__(self):
        return str(self.nominator) + "/" + str(self.denominator)
    def __add__(self,other):
        temp = Ratio(self.nominator * other.denominator + other.nominator * self.denominator, self.denominator * other.nominator + other.nominator * self.nominator)
        temp.simply()
        return temp
    def __mul__(self,other):
        temp = Ratio(self.nominator * other.nominator, self.denominator * other.denominator)
        temp.simply()
        return temp
    def __truediv__(self,other):
        temp = Ratio(self.nominator * other.denominator, self.denominator * other.nominator)
        temp.simply()
        return temp
    def

a = Ratio(1,2)
b = Ratio(2,4)
c = a + b
d = a * b
e = a / b
a.simply()
b.simply()
print(a)
print(b)
print(c)
print(d)
print(e)