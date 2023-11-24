import queue
import time

from Manager import QueueClient


def minion():
    client = QueueClient()

    while True:
        try:
            task = client.tasks.get_nowait()
        except queue.Empty:
            print("Task queue is empty. Minion is sleeping.")
            time.sleep(5)
            continue

        task.work()
        client.results.put((task.identifier, task.time))
        print(f"Minion processed task {task.identifier} in {task.time:.4f} seconds")


if __name__ == "__main__":
    minion()
