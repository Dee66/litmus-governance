def detect_forbidden_entropy(code: str) -> bool:
    forbidden_patterns = [
        'import time', 'from time import', 'import datetime', 'from datetime import',
        'import uuid', 'from uuid import', 'import random', 'from random import',
        'os.environ', 'os.getenv'
    ]
    return any(pattern in code for pattern in forbidden_patterns)

def detect_concurrency_primitives(code: str) -> bool:
    forbidden_patterns = [
        'import threading', 'from threading import', 'import asyncio', 'from asyncio import',
        'import multiprocessing', 'from multiprocessing import', 'from concurrent.futures import'
    ]
    return any(pattern in code for pattern in forbidden_patterns)

def detect_unordered_iteration(code: str) -> bool:
    # Simple detection: for loops over dict/set without sorted
    if 'for ' in code and ('dict(' in code or 'set(' in code) and 'sorted(' not in code:
        return True
    return False

def detect_non_canonical_serialization(code: str) -> bool:
    # Detect json.dump without sort_keys
    if 'json.dump' in code and 'sort_keys' not in code:
        return True
    # Detect direct file writes (simplistic)
    if '.write(' in code or 'open(' in code and "'w'" in code:
        return True
    return False