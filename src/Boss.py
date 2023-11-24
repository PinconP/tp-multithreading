import queue
import time

from Manager import QueueClient
from Task import Task


class Boss:
    def submit_task(self, task_id, task_size):
        task = Task(task_id, task_size)
        client.tasks.put(task)
        print(f"Boss added task {task_id} to the queue.")

    def wait_for_results(self, task_id):
        while True:
            try:
                result_id, result_time = client.results.get_nowait()
                print(f"Boss received result {result_id} in {result_time:.4f} seconds")
            except queue.Empty:
                print("Result queue is empty. Boss is sleeping.")
                time.sleep(5)
                continue
            if result_id == task_id:
                break


if __name__ == "__main__":
    client = QueueClient()
    boss = Boss()
    boss.submit_task(0, 6000)
    boss.wait_for_results(0)
    print("Boss is done.")
