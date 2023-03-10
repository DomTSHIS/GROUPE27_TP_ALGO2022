import time

from abc import abstractmethod, ABCMeta #on importe ce module pour l'utilisation de la methode abstraite
from math import pi #dans le module math,on importe l'opérateur pi

from math import sqrt #dans le module math,on importe l'opérateur racine carré

start_time = time.time()

class Forme_Geometrique: #création de la classe Forme_Géometrique

    def __init__(self,surface,perimetre): #La première de classe

        self.sur = surface

        self.per = perimetre

    @abstractmethod  #Pour montrer que nous utilisons la methode abstraite

    def perimetre(self,perimetre):

        return self.perimetre

    @abstractmethod

    def surface(self,surface):

        return self.surface

class Rectangle(Forme_Geometrique): #Création de la classe Rectangle

    def __init__(self,longueur,largeur): #Définition de la première methode de classe

        if longueur >=0 and largeur >=0:

            self.L = longueur

            self.l = largeur

        else:

            self.L = abs(longueur)

            self.l = abs(largeur)

    def surface(self):

        return self.L * self.l

    def perimetre(self):

        return (self.L + self.l)*2

    def sol_rectangle(self): #Définition de la methode solution

        print(f"Le le perimètre du rectangle vaut : {self.perimetre()} m")

        print(f"La surface du rectangle vaut : {self.surface()} m²")

    @classmethod

    def Carre(cls,mesure_cote): #Ceci montre le carré est un cas particulier du rectancle

        return cls(mesure_cote,mesure_cote)

class Cercle(Forme_Geometrique) : #Création de la classe cercle

    def __init__(self,rayon):

        if rayon >= 0:

            self.r = rayon

        else:

            self.r = abs(rayon)

    def perimetre(self):

        return "{:.3f}".format(2*pi*self.r)

    def surface(self):

        return "{:.3f}".format(pi*(self.r)**2)

    def sol_cercle(self): #Définition de la methode solution dans la classe cercle

        print(f"Le perimètre du cercle egale : {self.perimetre()} m")

        print(f"La surface du cercle egale : {self.surface()} m²")

class Triangle(Forme_Geometrique): #Création de la classe triangle

    def __init__(self,cote_x, cote_y, cote_z): #premiere methode

        if cote_x >=0 and cote_y >=0 and cote_z >=0 : #on pose une condition sur la mesure des cotés

            self.x = cote_x

            self.y = cote_y

            self.z = cote_z

        else:

            self.x = abs(cote_x)

            self.y = abs(cote_y)

            self.z = abs(cote_z)

    def perimetre(self):

        return self.x + self.y + self.z

    def surface(self):

        demi_p = (self.x + self.y + self.z)/2 #pour calculer le dimi perimetre

        surface = sqrt(abs(demi_p*(demi_p-self.x)*(demi_p-self.y)*(demi_p-self.z)))

        return "{:.3f}".format(surface)

    def sol_triangle(self): #la methode solution dans la classe triangle

        print(f"Le perimètre du triangle égale : {self.perimetre()} m")

        print(f"La surface du triangle égale : {self.surface()} m²")

    @classmethod

    def Triangle_Rectangle(cls,hyp,haut,base): #le triangle rectangle un cas particulier de la classe triangle

        return cls(hyp,haut,base)


"""BATTERIE DES TESTS"""


if __name__=='__main__': #Pour connaitre la memoire de l'objet

    a_1 = Cercle(4)

    a_1.sol_cercle()

    print("\n La batterie de test complete...")
    
    print("\nTest rectangle\n")
    r = Rectangle(8, 4)
    print(r.surface())
    print(r.perimetre())
    r.sol_rectangle()
   
    print("\nTest carré\n")
    car  = Rectangle.Carre(12)
    print("la surface du carré vaut:",car.surface(),"m²")
    print("le périmètre du carré vaut",car.perimetre(),"m")
    
    print("\nTest cercle\n")
    
    rond = Cercle(5)
    print(rond.perimetre())
    print(rond.surface())
    rond.sol_cercle()
    
    print("\nTest triangle\n")
    
    tri = Triangle(3, 6, 9)
    print(tri.perimetre())
    print(tri.surface())
    tri.sol_triangle()
    
    print("\nTest triangle Rectangle\n")
   
    Trec = Triangle.Triangle_Rectangle(2,4,8)
    print("le périmetre du triangle réctangle vaut :", Trec.perimetre(),"m")
    print("la surface du triangle réctangle vaut : ",Trec.surface(),"m²")
    
    end_time = time.time()
    
    print("le temps d'execution est :", end_time - start_time, "secondes")
    
