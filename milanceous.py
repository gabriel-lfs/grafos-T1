import os
from typing import List

import psutil


def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss


def partial(items: List[int]):
    return sum(items) / len(items)
