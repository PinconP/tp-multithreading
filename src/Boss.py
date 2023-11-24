from Manager import QueueClient
from Task import Task

if __name__ == "__main__":
    client = QueueClient()

    for i in range(5):  # Let's say we want to put 5 tasks
        client.tasks.put(Task(i, 6000))

    print("Boss has added tasks to the queue.")
