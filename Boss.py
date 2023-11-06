class Boss:
    def __init__(self, queue_client):
        self.queue_client = queue_client

    def assign_task(self, task):
        self.queue_client.put_task(task)
