from threading import Semaphore
from queue import Queue
from datetime import datetime

class QueueManager:
    def __init__(self, aging_time):
        self.aging_time = aging_time
        self.real_time_semaphore = Semaphore(1)
        self.semaphore1 = Semaphore(1)
        self.semaphore2 = Semaphore(1)
        self.semaphore3 = Semaphore(1)
        self.real_time = Queue()
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.queue3 = Queue()
        self.semaphores = [self.real_time_semaphore, self.semaphore1, self.semaphore2, self.semaphore3]
        self.queues = [self.real_time, self.queue1, self.queue2, self.queue3]

    
    def insert(self, process_id, priority):
        if priority > 3:
            return 
        print("inserting process", process_id, "with priority", priority)
        current_time = datetime.now()
        process = (process_id, priority, current_time)

        semaphore = self.semaphores[priority - 1]
        queue = self.queues[priority - 1]

        semaphore.acquire()
        queue.put(process)
        semaphore.release()

        print("Queue 1: ", self.queue1.queue)
        print("Queue 2: ", self.queue2.queue)
        print("Queue 3: ", self.queue3.queue)

        # self.queues.append((process_id, priority))
    
    def aging(self):
        current_time = datetime.now()
        for priority in range(2, 4):
            # Get list of all processID with aging time higher than self.aging_time
            print(self.queues)
            processes = [id for id, insertion_time in list(self.queues[priority].queue) \
                if self.diff_time(current_time, insertion_time) > self.aging_time]
            # Remove them and insert on a higher priority file
            if len(processes) > 0:
                print("** Priority ", priority, " queue has to these processes to be aged", processes, "\n")
            [self.remove(id, priority) for id in processes]
            [self.insert(id, priority-1) for id in processes]
        
    
    # def next_process(self):
    #     if not self.queue:
    #         return NO_NEXT_PROCESS
    #     self.queue = sorted(self.queue, key=lambda x: x[1], reverse=True)
    #     return self.queue.pop(0)[0]

    # def insert_process(self, priority, process):
    #     self.insert(process.get_id(), priority)

    def diff_time(time1, time2):
        delta = time1 - time2
        return delta.seconds + delta.microseconds/1000000