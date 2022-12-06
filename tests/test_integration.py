import file_queue

import operator


def test_submit_host_standard_pass():
    queue = file_queue.Queue(".queues")
    job = queue.enqueue(operator.add, 2, 5)
    result = job.wait()
    assert result == 7
