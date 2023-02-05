from modules.process import Process

class ProcessManager:
    def __init__(self):
        self.processes = {}
        self.counter = 0

    def create_process(self, process):
        priority, time_created, mem_allocated, time_limit, time_processor, io_devices, offset, op = process   
        process_id = self.get_next_process_id()
        process = Process(process_id, priority, mem_allocated, time_created, time_limit, time_processor, io_devices)
        process.offset = offset
        self.processes[process_id] = process
        return process_id

    def get_process(self, id):
        return self.processes[id]

    def get_processes(self):
        return self.processes

    def get_id(self, process):
        return process.get_id()

    def delete_process(self, id):
        del self.processes[id]

    def get_next_process_id(self):
        self.counter += 1
        return self.counter
    
    def num_active_processes(self):
        return len(self.processes)

    def decrease_processor_times(self, id):
        self.processes[id].decrease_processor_time()

    def decrease_time_limit(self, id):
        self.processes[id].decrease_time_limit()

    def get_processor_time(self, id):
        return self.processes[id].get_processor_time()

    def remove_finished_processes(self):
        for process in self.processes.values():
            if process.get_time_limit() == 0:
                self.delete_process(process.get_id())