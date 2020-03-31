import numpy as np
from colorama import Fore, Style


class Ruler:
    """
    Classe d'objet créé à partir de deux chaînes de caractères qui permet de comparer 
    ces deux dernières facilement grâce au deux attributs (first et second) de l'objet.
    """
    def __init__(self, first, second, distance=None, F=None):
        # problème avec le programme sur les 2 premiers caractères dans certaines situations
        # donc on ajoute des caractères (que l'on enlèvera par la suite) qui permettent de 
        # palier à cette erreur.
        self.first = " " + " " + first      
        self.second = " " + " " + second
        self.distance = distance
        self.mat = F


    def compute(self, d=1):
        
        # Fonction qui donne le coût binaire de l'opération
        def S(i, j):
            if self.first[i] == self.second[j]:
                return 0
            else :
                return 1
        
        # Création de la matrice de coût
        n = len(self.first)
        m = len(self.second)
        F = np.zeros((n, m))
        for i in range(n):
            F[i, 0] = d * i
        for j in range(m):
            F[0, j] = d * j
        for i in range(1, n):
            for j in range(1, m):
                c1 = F[i-1, j-1] + S(i, j)
                c2 = F[i-1, j] + d
                c3 = F[i, j-1] + d
                F[i, j] = min(c1, c2, c3)
        self.mat = F

        # Création des chaînes de caractères qui permettront la comparaison visuelle
        align1 = ""
        align2 = ""
        i = len(self.first) - 1
        j = len(self.second) - 1
        
        while i > 0 and j > 0:
            score = F[i, j]
            score_diag = F[i-1, j-1]
            score_up = F[i, j-1]
            score_left = F[i-1, j]
            if score == score_diag + S(i, j):
                align1 = self.first[i] + align1
                align2 = self.second[j] + align2
                i -= 1
                j -= 1
            elif score == score_left + d:
                align1 = self.first[i] + align1
                align2 = "=" + align2
                i -= 1
            elif score == score_up + d:
                align1 = "=" + align1
                align2 = self.second[j] + align2
                j -= 1
        
        while i > 0 and j <= 0:
            align1 = self.first[i] + align1
            align2 = "=" + align2
            i -= 1
        
        while j > 0 and j <= 0:
            align1 = "=" + align1
            align2 = self.second[j] + align2
            j -= 1

        if i == 0 and j == 0:
            align1 = self.first[i] + align1
            align2 = self.second[j] + align2
        
        
        def red_text(text):
            return f"{Fore.RED}{text}{Style.RESET_ALL}"
        
        # Calcul de la distance entre les deux chaînes et mise en rouge des différences
        a1 = ""
        a2 = ""
        dist = 0
        
        for i, x in enumerate(align1):
            if align2[i] != x and x != '=' and align2[i] != '=':
                a1 += f"{red_text(align1[i])}"
                a2 += f"{red_text(align2[i])}"
                dist += 1
            elif x == '=':
                a1 += f"{red_text(align1[i])}"
                a2 += f"{align2[i]}"
                dist += 1
            elif align2[i] == '=':
                a1 += f"{align1[i]}"
                a2 += f"{red_text(align2[i])}"
                dist += 1
            else:
                a1 += f"{align1[i]}"
                a2 += f"{align2[i]}"

        self.distance  = dist
        self.first = a1[2:]
        self.second = a2[2:]

    
    def report(self) :
        return (self.first, self.second)