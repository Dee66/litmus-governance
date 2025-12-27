from enum import Enum

class RunState(Enum):
    INVALID = "INVALID"
    REFUSED = "REFUSED"
    ADVISORY = "ADVISORY"
    BLOCKING = "BLOCKING"