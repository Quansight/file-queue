import pathlib
import contextlib
from typing import Union

import filelock

from file_queue.core import DummyLock


class FileLock(DummyLock):
    @contextlib.contextmanager
    def aquire(self, path: Union[str, pathlib.Path]):
        with filelock.FileLock(path):
            yield
