from projet01_tpalgo22_groupe27 import* #notre module de l'implementation du projet01.

import unittest #ici nous importons l'un des modules de python pour le test unitaire.

class Testing(unittest.TestCase): #création d'une classe dont les instances sont des cas de test uniques.

    def test_perimetre_rectangle(self): #nous définissons une fonction pour tester le perimetre du rectangle.

        a = Rectangle(-8,6).perimetre() #nous avons attribués des parametres numeriques à notre rectangle pour calculer le perimetre.

        sol_a = 28 #la valeur numerique du perimetre attendue, suite à l'introduction des parametres ci-haut.

        self.assertEqual(a,sol_a)

    def test_surface_rectangle(self):

        x = Rectangle(10,4).surface()

        sol_x = 40

        self.assertEqual(x,sol_x)

    def test_surface_cercle(self):

        y = Cercle(-5).surface()

        sol_y = '78.540'

        self.assertEqual(y,sol_y)

    def test_perimetre_cercle(self):

        t = Cercle(10).perimetre()

        sol_t = '62.832'

        self.assertEqual(t,sol_t)

    def test_perimetre_triangle(self):

        b = Triangle(8,-6,6).perimetre()

        sol_b = 20

        self.assertEqual(b,sol_b)

    def test_surface_triangle(self):

        c = Triangle(8,-6,6)

        sol_c ='17.889'

        self.assertEqual(c,sol_c)


if __name__ =='__main__':

    unittest.main()


