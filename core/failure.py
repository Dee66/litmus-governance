import sys
import os

def hard_fail(reason: str) -> None:
    print(reason, file=sys.stderr)
    os._exit(1)