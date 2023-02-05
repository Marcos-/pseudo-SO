class MemoryManager:
    def __init__(self, memory_size):
        self.memory_size = memory_size
        self.allocations = {}
        self.offset = 0

    def load(self, process_id, size, offset):
        if self.offset + size > self.memory_size:
            return NOT_ENOUGH_RAM_MEMORY
        self.allocations[process_id] = (self.offset, size)
        offset[0] = self.offset
        self.offset += size
        return SUCCESS
    
    def remove(self, process_id, size, offset):
        del self.allocations[process_id]
        self.offset = offset

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

class ResourceManager:
    def __init__(self):
        self.devices = {}

    def add_device(self, device_id, device):
        self.devices[device_id] = device

    def get_device(self, device_id):
        return self.devices[device_id]

