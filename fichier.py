""" Afficher les coordonnés d'un point P
et une fonction distance() qui permette de calculer la distance entre deux points.
Cette fonction attendra évidemment deux objets Point() comme arguments. """
from math import*
class Point:
    "définition d'un point mathématique"
p9=Point()
p1=Point()
p2=Point()
def Affiche_Les_CoordonnésDu_point(p):
    #print("coord.horizontale =",p.x,"coord.verticale =",p.y)
    print("P(",p.x,",",p.y,")")
p9.x=3
p9.y=4
Affiche_Les_CoordonnésDu_point(p9)
def Distance():
    print("la distance entre P1 et P2 vaut:",sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2))
p1.x=float(input("Entrez l'abscice du 1èr point:\n"))
p1.y=float(input("Entrez l'ordonné du 1èr point:\n"))
p2.x=float(input("Entrez l'abscice du 2èm point:\n"))
p2.y=float(input("Entrez l'ordonné du 2èm point:\n"))
Affiche_Les_CoordonnésDu_point(p1)
Affiche_Les_CoordonnésDu_point(p2)
Distance()
