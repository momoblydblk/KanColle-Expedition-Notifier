from timer import Timer
from time import time

class Expedition:

    expeditionID = 0          # Expedition ID, int, 1-41
    expeditionTime = 0        # Expedition Time, int, unit:seconds
    bindTimer = None
    fleet=0

    def __init__(self, eid: int, time: int, fleet: int, timerInstance: Timer):
        self.expeditionID = eid
        self.expeditionTime = time
        self.fleet = fleet
        self.bindTimer = timerInstance