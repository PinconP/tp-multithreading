import unittest

from src.task import Task  # Importation de la classe Task à tester


class TestTask(unittest.TestCase):  # Définition de la classe de test pour Task
    def test_serialization(self):
        # Test pour vérifier la fonctionnalité de sérialisation et désérialisation

        # Création d'une instance de Task
        a = Task("1")

        # Sérialisation de l'instance 'a'
        a_json = a.to_json()

        # Création d'une nouvelle instance de Task à partir de la sérialisation
        b = Task.from_json(a_json)

        # Vérification de l'égalité entre 'a' et 'b'
        self.assertEqual(a, b)

    def setUp(self):
        # Méthode exécutée avant chaque test pour initialiser les ressources
        self.task = Task(identifier="test", size=10)

    def test_creation(self):
        # Test pour vérifier la création correcte d'une instance de Task

        self.assertEqual(self.task.identifier, "test")
        self.assertEqual(self.task.size, 10)
        self.assertIsNotNone(self.task.a)
        self.assertIsNotNone(self.task.b)
        self.assertIsNotNone(self.task.x)
        self.assertEqual(self.task.time, 0)

    def test_work(self):
        # Test pour vérifier la méthode 'work' de la classe Task

        self.task.work()
        self.assertGreater(self.task.time, 0)
        # Des vérifications supplémentaires peuvent être ajoutées pour s'assurer de la correction de la solution

    def test_equality(self):
        # Test pour vérifier l'égalité entre deux instances de Task

        another_task = Task(identifier="test", size=10)
        another_task.a = self.task.a
        another_task.b = self.task.b
        another_task.x = self.task.x
        another_task.time = self.task.time
        self.assertEqual(self.task, another_task)

        # Modification d'un attribut pour garantir l'inégalité
        another_task.identifier = "different"
        self.assertNotEqual(self.task, another_task)

        # Test avec un objet qui n'est pas une instance de Task
        not_a_task = "some_string"
        self.assertNotEqual(self.task, not_a_task)


if __name__ == "__main__":
    unittest.main()  # Exécution des tests si le script est exécuté directement
