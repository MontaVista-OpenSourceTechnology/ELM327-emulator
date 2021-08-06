from elm import Tasks
import random

class Task(Tasks):
    engine_load = 50
    def start(self, cmd, *_):
        self.engine_load = random.randrange(50, 100, 5)
        return (self.PA(cmd),
                Tasks.RETURN.CONTINUE,
                None if self.task_request_matched(cmd) else cmd)
    def run(self, cmd, *_):
        self.engine_load += random.choice((-5,5))
        return (self.PA(hex(self.engine_load)[2:]),
                Tasks.RETURN.CONTINUE,
                None if self.task_request_matched(cmd) else cmd)
        