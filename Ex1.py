class Student:
    def __init__(self,nom,filier,notes):
        self.nom=nom
        self.filier=filier
        self.notes=notes
    def operation(self,notes):
        maxi = notes[0]
        longueur=len(self.notes)
        for i in range(longueur):
            if self.notes[i] >= maxi:
                maxi = notes[i]
            return maxi