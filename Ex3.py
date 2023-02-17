from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


class Poly2n:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def calculdelta(self):
        delta=self.b**2-4*self.a*self.c
        return delta 
    def roots(self):
        self.calculdelta()
        if self.calculdelta()>0:
            rot1=-self.b+sqrt(self.calculdelta())/2*self.a
            rot2=-self.b-sqrt(self.calculdelta())/2*self.a
            return rot1,rot2
        elif self.calculdelta()<0:
            return False
        else :
            rot=-self.b/2*self.a
            return rot
    def draw(self):
        x=np.linspace(6,5,2)
        y=self.a*x**2 + self.b*x + self.c
        plt.figure()
        plt.plot(x,y)
        type(x)
        return plt.show()
    
         
p10=Poly2n(4,-2,1) 
# print(p10.calculdelta()) 
# print(p10.roots()) 
p10.draw()     
                    
                
                  
    