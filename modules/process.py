

class Process:
    def __init__(self, id, priority, mem_allocated, time_created, time_limit, time_processor, io_devices):
        self.id = id
        self.priority = priority
        self.mem_allocated = mem_allocated
        self.time_created = time_created
        self.time_limit = time_limit
        self.time_processor = time_processor
        self.io_devices = io_devices
        self.offset = 0