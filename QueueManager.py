import multiprocessing

from BaseManager import BaseManager


class QueueManager(BaseManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task_queue = multiprocessing.Queue()
