from elm import Tasks
import random

class Task(Tasks):
    vehicle_speed = 20
    def start(self, cmd, *_):
        self.vehicle_speed = random.randrange(20, 40, 5)
        return (self.PA(hex(self.vehicle_speed)[2:]),
                Tasks.RETURN.CONTINUE,
                None if self.task_request_matched(cmd) else cmd)
    def run(self, cmd, *_):
        self.vehicle_speed += random.choice((-5,5))
        return (self.PA(hex(self.vehicle_speed)[2:]),
                Tasks.RETURN.CONTINUE,
                None if self.task_request_matched(cmd) else cmd)
        