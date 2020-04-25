import math

class quadraticEquate:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def roots(self):
        d = self.b**2 - 4*self.a*self.c
        if d<0:
            return None
        else:
            r1 = (-self.b + math.sqrt(d))/(2*self.a)
            r2 = (-self.b - math.sqrt(d))/(2*self.a)
        return r1,r2
    
if __name__ == '__main__':
    exit()
    #If this is run as main file, then exit. 

