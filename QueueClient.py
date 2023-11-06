class QueueClient:
    def __init__(self, queue_manager):
        self.queue_manager = queue_manager

    def get_task(self):
        return self.queue_manager.task_queue.get()

    def put_task(self, task):
        self.queue_manager.task_queue.put(task)
