import time


class ExecutionTimer:
    def __init__(self):
        self.start = None
        self.end = None

    def start_timer(self):
        self.start = time.time()
        return

    def end_timer(self):
        self.end = time.time()
        return

    def elapsed_time(self):
        total_s = int(self.end - self.start)
        secondes = total_s % 60
        minutes = (total_s / 60) % 60
        minutes = int(minutes)
        hours = (total_s / (60 * 60)) % 24
        hours = int(hours)
        return "{} Heures  {} Minutes  {} Secondes".format(hours, minutes, secondes)
