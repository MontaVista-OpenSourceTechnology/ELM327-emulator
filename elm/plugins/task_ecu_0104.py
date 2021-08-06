from elm import Tasks, EcuTasks
import random

class Task(EcuTasks):
    engine_load = 50
    def run(self, cmd, *_, engine_load):
        engine_load += random.randint(-5, 5)
        return (self.PA(str(engine_load)),
                Tasks.RETURN.CONTINUE,
                None if self.task_request_matched(cmd) else cmd)
        