class Minion:
    def __init__(self, queue_client):
        self.queue_client = queue_client

    def do_task(self):
        task = self.queue_client.get_task()
        if task is not None:
            task.work()
            return True
        return False
