class QueueManager:
    def __init__(self, aging_time):
        self.queue = []
        self.aging_time = aging_time
    
    def insert(self, process_id, priority):
        self.queue.append((process_id, priority))
    
    def aging(self):
        for i in range(len(self.queue)):
            self.queue[i] = (self.queue[i][0], self.queue[i][1] + self.aging_time)
    
    def next_process(self):
        if not self.queue:
            return NO_NEXT_PROCESS
        self.queue = sorted(self.queue, key=lambda x: x[1], reverse=True)
        return self.queue.pop(0)[0]

    def insert_process(self, priority, process):
        self.insert(process.get_id(), priority)