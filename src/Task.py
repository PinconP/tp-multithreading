import json
from time import perf_counter

# Importation de la bibliothèque NumPy pour les opérations sur les tableaux
import numpy as np


class Task:
    def __init__(self, identifier, size=None):
        self.identifier = identifier  # Enregistrement de l'identifiant de la tâche
        # Définir la taille du problème, par défaut un entier aléatoire entre 300 et 3000
        self.size = size or np.random.randint(300, 3000)

        # Générer les entrées du problème sous forme de matrices et vecteurs
        self.a = np.random.rand(
            self.size, self.size
        )  # Matrice A aléatoire de dimensions size x size
        # Vecteur B aléatoire de dimension size
        self.b = np.random.rand(self.size)

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

    def to_json(self) -> str:
        # Convertir les attributs NumPy en listes pour la sérialisation
        data = {
            "identifier": self.identifier,
            "size": self.size,
            "a": self.a.tolist(),  # Convertir la matrice NumPy en liste
            "b": self.b.tolist(),  # Convertir le vecteur NumPy en liste
            "x": self.x.tolist(),  # Convertir le vecteur de résultat en liste
            "time": self.time,
        }
        return json.dumps(data)  # Sérialiser le dictionnaire en chaîne JSON

    @classmethod
    def from_json(cls, text: str) -> "Task":
        # Désérialiser le texte JSON en un dictionnaire
        data = json.loads(text)

        # Créer une instance de Task en utilisant les données du dictionnaire
        task = cls(identifier=data["identifier"], size=data["size"])

        # Convertir les listes en matrices/vecteurs NumPy
        task.a = np.array(data["a"])
        task.b = np.array(data["b"])
        task.x = np.array(data["x"])
        task.time = data["time"]

        return task

    def __eq__(self, other: "Task") -> bool:
        if not isinstance(other, Task):
            # Retourner False si 'other' n'est pas une instance de Task
            return False

        # Comparer l'identifiant, la taille et le temps
        are_basic_attrs_equal = (
            self.identifier == other.identifier
            and self.size == other.size
            and self.time == other.time
        )

        if not are_basic_attrs_equal:
            return False

        # Comparer les matrices et les vecteurs en utilisant np.array_equal
        are_arrays_equal = (
            np.array_equal(self.a, other.a)
            and np.array_equal(self.b, other.b)
            and np.array_equal(self.x, other.x)
        )

        return are_arrays_equal
