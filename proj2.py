# class Rectangle:
#     def __init__(self,longueur, largeur):
#         self.longueur=longueur
#         self.largeur=largeur
#     def perimetre(self):
#         return 2*(self.longueur+ self.largeur) 
#     def surface(self):
#         return self.longueur*self.largeur
        
# class  Parallelepipede(Rectangle):
#     def __init__(self, longueur, largeur,hauteur):
#         super().__init__(longueur, largeur) 
#         self.hauteur= hauteur
#     def volume(self):
#         return self.longueur *self.largeur*self.hauteur
         
# p=Rectangle(12,2) 
# p1=Parallelepipede(12,2,4) 
# print(p.perimetre())
# print(p.surface()) 
# print(p1.volume())
         
#exercice2 
# class  CompteBancaire:
#     def __init__(self,numeroCompte,nom,solde) :
#         self.numeroCompte=numeroCompte
#         self.nom=nom
#         self.solde=solde
#     def versement(self,argent):
#         solde= self.solde+argent 
#         return solde
#     def retrait(self,argent):
#         if(self.solde < argent):
#             print(" Impossible d'effectuer l'opération. Solde insuffisant !")
#         else:
#             self.solde = self.solde - argent
#     def Agios(self):
#         self.solde =self.solde*95/100
#     def afficher(self):
#         print("numero de compe",self.numeroCompte)  
#         print("prenom et nom du client",self.nom)
#         print("solde du client",self.solde,"DH")
# monCompte = CompteBancaire(16168891, "  Thiaw", 22300)
# monCompte.versement(1500)
# monCompte.retrait(24000)
# #monCompte.agios()
# monCompte.afficher()  

# #exercice3
# from math import pi
# class Cercle:
#     def __init__(self,a,b,r):
#         self.a=a
#         self.b=b
#         self.r=r
#     def Surface(self):
#         return pi*self.r*self.r
#     def perimetre(self):
#         return 2*(pi*self.r)
#     def formEquation(self,x,y):      
#         return (x-self.a)**2 + (y-self.b)**2 -self.r**2
#     def test_appartenance(self,x,y):
#         if(self.formEquation(x,y)==0):
#             print("le point : (",x,y,") appartient au cercle C")
#         else:
#             print("le point : (",x,y,") n'appartient pas au cercle C")
            
        
# # Instanciation   
# C = Cercle(1,2,1)
 
# print("le périmètre du cercle C est  : ", C.perimetre())
# print("le surface du cercle C est  : ", C.surface())
# C.test_appartenance(1,1) # affiche: le point : ( 1 1 ) appartient au cercle C
# #Exercice4
class Calcul:
    def __init__(self):
        pass
#---Factorielle ------------    
    def factorielle(self, n):
        j=1
        for i in range(1,n+1):
            j = j*i
        return j
#---Somme des n premiers nombres----
    def somme(self, n):
        j=1
        for i in range(1,n+1):
            j = j+i
        return j
#---Test primalité d'un nombre------------
    def testPrim(self, n):
        j=0
        for i in range(1,n+1):
            if(n%i==0):
                j = j + 1
        if(j == 2):
            return True
        else:
            return False 
            
# ---Test primalité de deux nombres entiers------------
    def testprims(self , n , m):
        divCommun = 0
        for i in range(1 , n+1):
            if (n%i == 0 and m%i == 0):
                divCommun = divCommun + 1
        if divCommun == 1:
            print("Les nombres " , n , " et ", m , " sont premiers entre eux")
        else:
            print("Les nombres " , n , " et ", m , " ne sont pas premiers entre eux")
            
#---Table de multiplication-------------
    def tableMult(self,k):
        for i in range(1,10):
            print(i," x ",k," = ",i*k)
 
#---Toutes les tables de multiplication des nombres 1, 2, .., 9
    def toutesLesTables(self):
        for k in range(1,10):
            print("\nla table de multiplication de : ",k, " est : ")
            for i in range(1,10):
                print(i," x ",k," = ",i*k)
                
#----- liste des diviseurs d'un entier                
    def listDiv(self , n):
        # initialisation de la liste des diviseurs
        lDiv = []
        for i in range(1 , n+1):
            if ( n%i == 0):
                lDiv.append(i)
        return lDiv
    
# ------liste des diviseurs premiers d'un entier----------------    
    def listDivPrim(self , n):
        # initialisation de la liste des diviseurs
        lDiv = []
        for i in range(1 , n+1):
            if ( n%i == 0 and self.testPrim(i)):
                lDiv.append(i)
        return lDiv                 
                
# Exemple Instanciation
Cal = Calcul()
Cal.testprims(13 , 7)
print("Liste des diviseurs de 18 : ", Cal.listDiv(18))
print("Liste des diviseurs premiers de 18 : ", Cal.listDivPrim(18))
Cal.toutesLesTables()
    
             
            
    
        
          
              
                
