from modules.process import Process

class ProcessManager:
    def __init__(self):
        self.processes = {}
        self.counter = 0

    def create_process(self, priority, time_created, mem_allocated, time_limit, time_processor, io_devices, offset, op):
        process_id = self.get_next_process_id()
        process = Process(process_id, priority, mem_allocated, time_created, time_limit, time_processor, io_devices)
        process.offset = offset
        self.processes[process_id] = process
        return process_id

    def get_process(self, id):
        return self.processes[id]

    def delete_process(self, id):
        del self.processes[id]

    def get_next_process_id(self):
        self.counter += 1
        return self.counter
    
    def num_active_processes(self):
        return len(self.processes)