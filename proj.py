# heritage simple
# class Voiture:
#     def __init__(self, wheels,max_speed,cylindre) :
#         self.wheels=wheels
#         self.max_speed=max_speed
#         self.cylindre=cylindre
#     def demarrer(self):
#         pass
        
#     def arreter (self): 
#         pass
# class Moto(Voiture):...
# m1=Moto(2,150,300)
# print(m1.max)   
# print(m1.cylindre) 
# class Camion (Voiture):
#     pass  
# class A :
#     def __init__(self,calculer):
#         self.calculer=calculer
        
# class B(A):...
#     def __init__(self;poids) -> None:
#         pass
    
    
# class C(B):
#     pass
# class D(C):
#     pass
    
#      #heritage + quelque chose    
# class Car :
#     def drive(self):
#         return "I'am driving"
# class Superclas(Car):
#     def autodrive(self):
#         return "self.driving,atodive"
# v1=Superclas()
# v1.drive  

# # heritage+ajout d"attribut dans la class fille ajouter une nouvelle contructeur
# class Person:
#     def __init__(self,name) -> None:
#         self.name=name
# class Student(Person):
#     def __init__(self, name,email,address):
#         super().__init__(name) #initialisateur de la class  merci d'initialiser l'attribut name
#         self.email=email
#         self.address=address
# s1=Student("thiaw","thiawnd99@gmail.com","fann")
# print(s1.name,s1.email,s1.address)           
     #super()   
# class Person1:
#     def __init__(self,firsname,lasname,age) -> None:
#         self.name=firsname
#         self.lasname=lasname
#         self.age=age
# class Student(Person1):
#     def __init__(self,firsname,lasname,age,email):
#         super().__init__(firsname,lasname,age)
#         self.email=email
# a=Student("thiao","ndoumbe",23,"nd@99")  
# print(a.age,a.name,a.lasname,a.email)      
# #surchage redefinir une methode qui v
# class P:
#     def dirbonjour(self):
#         return "bonjour"
# class M(P):...
#     def bonjour(self):
#         return "salut"
# #encapsilation
# class Personne:
#     def __init__(self, niveau_sucre):
#         self.__niveau_sucre = niveau_sucre

#     def boire_lait(self, type_lait):
#         if type_lait == "entier":
#             self.__niveau_sucre += 3
#         elif type_lait == "demi_écrémé":
#             self.__niveau_sucre += 1
#         elif type_lait == "écrémé":
#             self.__niveau_sucre += 2
#         else:
#             self.__niveau_sucre = self.__niveau_sucre

#     def mesure_niveau_sucre(self):
#         print(self.__niveau_sucre)

# p = Personne(0)
# p.mesure_niveau_sucre()
# p.boire_lait("entier")
# p.mesure_niveau_sucre()    
    
# polymorphisme
# class Personne:
#     def __init__(self,nom,prenom):
#         self.nom=nom
#         self.prenom=prenom
#     def salut(self):
#         return "bonjour je m'appelle {self.nom}{self.prenom}"
#     def __str__(self) -> str:
#         return str(self.__class__)       
# class Etudiant(Personne):
#     def __init__(self, nom, prenom,filier):
#         super().__init__(nom, prenom)
#         self.filier  = filier 
#     def   salut(self):
#         return "bonjour je suis etudiant en filier et je m'appelle{self.nom}{self.prenon}"
# class Professeur(Personne) :
#     def __init__(self, nom, prenom,matier):
#         super().__init__(nom, prenom)
#         self.matier=matier
#         return "bonjour je suis professeur et je m'appelle {self.non}{self.prenom} j'enseigne {self.matier}"
#                               
# def introduction (o) :
#     return o.salut() 
# p1=Personne("camara","bineta")
# p2=Etudiant("camara","bineta","big data") 
# p3=Professeur("thiaw","ndoumbe","python")  
# print(p1.salut,p2.salut,p3.salut)   
# for i in [p1,p2,p3] : 
#     print(introduction(i))      
  
# class A:
#     def f(self):
#         return 42
# class B:
#     def h(self):
#         return 42
#     def __str__(self) :
#         return str("je suis un objet de la class B")
# a=A()
# b=B()
# print(a)
# print(b)    
                                                 
                                                 
class Ville:
    def __init__(self,nom:str,nbr_h:int,superf:float,langues:list):
        self.nom=nom
        self._nbr_h=nbr_h
        self.superficie=superf
        self.langue=langues
    def langue_d(self):
        # langue plus parles    
v1=Ville("dakar",1_056_000,83,["diola", " poular","sérère", "wolof"])
v2=v1=Ville(2,"1_056_000,83",["diola", " poular","sérère", "wolof"])

        
# pour acceder a l'attribut prive on cree une methode permettant d'afficher le contenu de l'attribue        
# len( ) exple de polymorphisme

        
                                                                  