class Person:
    def bonjour(self):
        print("bonjour")
    def aurevoir(self):
        print("aurevoir")
    def manger(self,food="orange"):
        print("Je mange",food)    
p1=Person()
print(type(p1))
p1.aurevoir()
p1.bonjour()
p1.manger()

class Person2:
    def __init__(self,name,age,email):
        self.name=name
        self.age= age
        self.email=email
p3=Person2("ousmane sonko",48,"oumane@gmail.com")
print(type(p3))
print(p3.age)

class Person3:
    def __init__(self,name,age,email):
            self.name=name
            self.age= age
            self.email=email
    def saluer(self,x):
        print(f"bonjour {x},comment vas tu")
    #def programmer(self,p="Python"):
        
# p4=Person3("fatima",21,"fatima99@gmail.com")
# p4.programmer("java")
# p4.saluer("amy")
    def programmer(self,p="Python"):
        print(f"je m'appelle {self.name} programme en {p}")
        self.saluer("patrick")
p4=Person3("Partick",21,"python")
p4.saluer("patrick")
p4.programmer("p")


class Student:
    def __init__(self,nom,filier,notes):
        self.nom=nom
        self.filier=filier
        self.notes=notes
    def operation(self):
        meilleur=max(self.notes)
        pire=min(self.notes)
        return (meilleur,pire)
    def moyen(self):
        moyen=sum(self.notes/len(self.notes))
        return moyen

p1=Student("fatima","info",[12,4,11,18])
p1.operation("meilleur")


class Student:
    def __init__(self,nom,filier,notes,prenom):
        self.nom=nom
        self.filier=filier
        self.notes=notes
        self.prenom=prenom
    def operation(self,notes):
        maxi = notes[0]
        longueur=len(self.notes)
        for i in range(longueur):
            if self.notes[i] >= maxi:
                maxi = notes[i]
            return maxi
            
# encapsilation
class Personne:
    def __init__(self, niveau_sucre):
        self.__niveau_sucre = niveau_sucre
    def boire_lait(self, type_lait):
        if type_lait == "entier":
            self.__niveau_sucre += 3
        elif type_lait == "demi_écrémé":
            self.__niveau_sucre += 1
        elif type_lait == "écrémé":
            self.__niveau_sucre += 2
        else:
            self.__niveau_sucre = self.__niveau_sucre
    def mesure_niveau_sucre(self):
        print(self.__niveau_sucre)
p = Personne(0)
p.mesure_niveau_sucre()
p.boire_lait("entier")
p.mesure_niveau_sucre()
    
    
        

    




                   





 




