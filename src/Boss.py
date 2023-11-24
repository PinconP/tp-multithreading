import queue
import time

from Manager import (  # Importation du client de la file d'attente depuis le module Manager
    QueueClient,
)
from Task import Task  # Importation de la classe Task depuis le module Task


class Boss:
    def __init__(self):
        self.client = QueueClient()  # Initialisation du client de file d'attente

    def submit_task(self, task_id, task_size):
        task = Task(
            task_id, task_size
        )  # Création d'un objet Task avec l'identifiant et la taille de la tâche
        # Ajout de la tâche à la file d'attente des tâches
        self.client.tasks.put(task)
        print(f"Boss added task {task_id} to the queue.")

    def wait_for_results(self, task_id):
        while True:  # Boucle infinie pour attendre le résultat
            try:
                # Tente de récupérer un résultat de la file d'attente
                result_id, result_time = self.client.results.get_nowait()
                print(f"Boss received result {result_id} in {result_time:.4f} seconds")
            except queue.Empty:
                # Si la file d'attente est vide, le programme se met en pause
                print("Result queue is empty. Boss is sleeping.")
                time.sleep(5)
                continue
            if result_id == task_id:
                # Si le résultat attendu est reçu, sortir de la boucle
                break


if __name__ == "__main__":
    boss = Boss()  # Création d'une instance de Boss
    boss.submit_task(
        0, 6000
    )  # Soumission d'une tâche avec un ID spécifique et une taille
    boss.wait_for_results(0)  # Attente des résultats pour la tâche soumise
    print("Boss is done.")  # Indication que le processus est terminé
