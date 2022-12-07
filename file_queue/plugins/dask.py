import logging

from file_queue.core import Worker, Queue

import dask.distributed
import dask


logger = logging.getLogger(__name__)


class MuliProcessingDaskWorker(Worker):
    def __init__(self, queue: Queue, threads_per_worker: int = 4, n_workers: int = 1):
        super().__init__(queue)
        self.client = dask.distributed.Client(
            threads_per_worker=threads_per_worker, n_workers=n_workers
        )

    def run(self):
        pass


class DaskJob(Job):
    pass
