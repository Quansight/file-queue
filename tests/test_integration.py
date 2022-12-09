import file_queue
from file_queue.plugins.ssh import SSHQueue

import operator


def test_submit_host_standard_pass():
    queue = file_queue.Queue(".queues/host")
    job = queue.enqueue(operator.add, 2, 5)
    result = job.wait()
    assert result == 7


def test_submit_ssh_standard_pass():
    queue = SSHQueue("ssh://root@localhost:2222/mnt/ssh_shared")
    job = queue.enqueue(operator.add, 3, 7)
    result = job.wait()
    assert result == 10


def test_submit_dask_standard_pass():
    queue = file_queue.Queue(".queues/dask")
    job = queue.enqueue(operator.add, 7, 11)
    result = job.wait()
    assert result == 18
