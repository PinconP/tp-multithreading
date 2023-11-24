from time import perf_counter

import numpy as np  # Importation de la bibliothèque NumPy pour les opérations sur les tableaux


class Task:
    def __init__(self, identifier, size=None):
        self.identifier = identifier  # Enregistrement de l'identifiant de la tâche
        # Définir la taille du problème, par défaut un entier aléatoire entre 300 et 3000
        self.size = size or np.random.randint(300, 3000)

        # Générer les entrées du problème sous forme de matrices et vecteurs
        self.a = np.random.rand(
            self.size, self.size
        )  # Matrice A aléatoire de dimensions size x size
        self.b = np.random.rand(self.size)  # Vecteur B aléatoire de dimension size

        # Initialiser un vecteur pour stocker les résultats, initialisé à des zéros
        self.x = np.zeros((self.size))
        self.time = 0  # Initialiser le temps de calcul à 0

    def work(self):
        start = perf_counter()  # Démarrer un compteur de temps
        self.x = np.linalg.solve(
            self.a, self.b
        )  # Résoudre le système d'équations linéaires Ax = B
        self.time = (
            perf_counter() - start
        )  # Calculer le temps écoulé pour la résolution
