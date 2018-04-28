import time
import sys

class Collector:
    def __init__(self, debug=False):
        self.time = 0
        self.debug = debug
        self.work = 20.0
        self.rest = 3.0

    def now(self):
        return time.time()

    def get(self):
        now = self.now()
        if self.debug:
            print >> sys.stderr, "idle: %.1f" % (now-self.time)
        return self.time, self.work, self.rest, now

    def tick(self):
        self.time = self.now()
        if self.debug:
            print >> sys.stderr, "tick now: %.1f" % self.time
        return self.get()

    def save_scales(self, work, rest):
        self.work = work
        self.rest = rest
        return ""
