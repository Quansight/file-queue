# File Queue

A task queue using the filesystem as the message queue.

# API

Creating a queue is as simple as supplying a directory where the queue
will reside.

```python
from file_queue import Queue

queue = Queue("path/to/queue")
```

Submitting jobs and monitoring over SSH is also supported via the same
interface. Workers currently cannot connect over SSH.

```python
from file_queue.plugins import SSHQueue

queue = SSHQueue("ssh://<username>:<password>@<hostname>:<port>/<path>")
```

Next we can submit/enqueue jobs to the queue.

```python
import operator

job = queue.enqueue(operator.add, 1, 2)
```

You can immediately try and fetch the result of the job or get its
status.

```python
print(job.get_status())
print(job.result)
```

You can wait on the job to finish

```python
result = job.wait()
```

# Worker

Starting a worker is as simple as giving a filesystem directory where
the queue will reside.

```shell
file-queue-worker --path ./path/to/queue
```

A worker run a continuous loop gathering tasks in the task queue. The
worker creates a file `path/to/queue/workers/<worker-id>` where it will:
 - continuously touch the file every 30 seconds
 - check that the file exists and if not stop the worker
