import queue
import time

from manager import (  # Importation du client de la file d'attente depuis le module Manager
    QueueClient,
)


class Minion:
    def __init__(self):
        self.client = QueueClient()  # Initialisation du client de file d'attente

    def work(self):
        while True:  # Boucle infinie pour traiter les tâches de manière continue
            try:
                task = (
                    self.client.tasks.get_nowait()
                )  # Tente de récupérer une tâche de la file d'attente
            except queue.Empty:
                # Si la file d'attente est vide, le minion se met en pause
                print("Task queue is empty. Minion is sleeping.")
                time.sleep(5)  # Pause de 5 secondes
                continue  # Continue la boucle

            task.work()  # Traitement de la tâche
            self.client.results.put(
                (task.identifier, task.time)
            )  # Ajout du résultat à la file d'attente des résultats
            print(
                f"Minion processed task {task.identifier} in {task.time:.4f} seconds"
            )  # Affiche le temps de traitement


if __name__ == "__main__":
    minion = Minion()  # Création d'une instance de Minion
    minion.work()  # Démarre le traitement des tâches
