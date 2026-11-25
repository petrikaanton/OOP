class Obdlznik:
    def __init__(self,len,hig):
        self.len = len
        self.hig = hig
    def area(self):
        return self.len * self.hig
    def perimeter(self):
        return (self.len * 2) + (2 * self.hig)

r = Obdlznik(3,4)
print(r.area(),r.perimeter())