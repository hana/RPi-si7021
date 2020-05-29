
import time

class Metro:
    def __init__(self, duration):
        self.duration = duration
        self.prev = time.time() * 1000.0

    def update(self, func, *args):
        now = time.time() * 1000
        diff = now - self.prev

        if(self.duration < diff):
            if(len(args)):
                func(args)
            else:
                func()
                
            self.prev = now
            return True
        else:
            return False
        
