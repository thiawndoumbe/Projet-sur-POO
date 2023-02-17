from math import sqrt
class Point:
    def __init__(self, x, y,z):
        self.x = x 
        self.y = y 
        self.z=z
    def distance(self):
        dis= sqrt(self.x**2+self.y**2+self.z**2)  
        return dis
    def move(self,a,b,c):
        self.x=self.x+a
        self.y=self.y+b
        self.z=self.z+c
        
        
p=Point(3,5,7)
print(p.distance())
p.move(2,1,3)
print(p.x,p.y,p.z) 
    
        

