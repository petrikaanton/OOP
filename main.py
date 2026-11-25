class Komplex:
    def __init__(self,r,k):
        self.r = r
        self.k = k

    def __add__(self,other):
        return Komplex(self.r+other.r,self.k+other.k)
    def __sub__(self,other):
        return Komplex(self.r-other.r,self.k-other.k)
    def __mul__(self,other):
        return Komplex(self.r*other.r,self.k*other.k)
    def __str__(self):
        if self.k >= 0:
            return str(self.r)+'+'+str(self.k)
        else:
            return str(self.r)+'-'+str(self.k)

k1 = Komplex(2,3)
k2 = Komplex(2,1)
k3 = k1 * k2
print(k3)