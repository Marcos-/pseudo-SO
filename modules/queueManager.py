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
        if priority <= 3:
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
        
        else:
            print("Error: priority must be 3 or higher")

        # self.queues.append((process_id, priority))
    
    def remove(self, process_id, priority):
        queue = self.queues[priority]
        semaphore = self.semaphores[priority]

        def remove_process(process_id):
            aux, insertion_time = queue.get()
            if aux != process_id:
                queue.put((aux, insertion_time))
            
            semaphore.release()
            for i in range(len(queue.queue)):
                remove_process(process_id)
    
    def aging(self):
        current_time = datetime.now()
        for priority in range(2, 4):
            # Get list of all processID with aging time higher than self.aging_time
            print("Queue ", priority, " has these processes: ", list(self.queues[priority].queue))

            processes = []
            for item in list(self.queues[priority].queue):
                print("item: ",item)
                if self.diff_time(current_time, item[2]) > self.aging_time:
                    processes.append(item[0])


            # Remove them and insert on a higher priority file
            if len(processes) > 0:
                print("** Priority ", priority, " queue has to these processes to be aged", processes, "\n")
            [self.remove(id, priority) for id in processes]
            [self.insert(id, priority-1) for id in processes]

    def next_process(self) -> int:
        for priority in range(4):
            if(not self.queues[priority].empty()):
                return self.__get_next(priority)[0]
        return 'NO_NEXT_PROCESS'

    def __get_next(self, priority: int) -> int:
        self.semaphores[priority].acquire() 
        aux = self.queues[priority].get()
        self.semaphores[priority].release()
        return aux 

    def diff_time(self, time1, time2):
        delta = time1 - time2
        return delta.seconds + delta.microseconds/1000000