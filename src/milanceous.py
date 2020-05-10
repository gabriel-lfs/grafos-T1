import os
from datetime import datetime
from typing import List

import psutil


def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss


def partial(items: List[int]) -> int:
    return int(sum(items) / len(items))


def create_file_audit(name):
    return f'reports/{name}_{datetime.now().isoformat("_").replace(":", "").replace(".", "")}.txt'
