from modules.process import Process

class ProcessManager:
    def __init__(self):
        self.processes = {}
        self.counter = 0

    def create_process(self, process):
        process_id = process['id']
        priority = process['priority']
        mem_allocated = process['memory_blocks']
        time_created = process['init_time']
        time_limit = process['init_time']
        time_processor = process['processor_time']
        io_devices = [process['printer_code'], process['scanner'], process['modem'], process['disk_code']]
        # offset = process['offset']
        
        
        process_id = self.get_next_process_id()
        process = Process(process_id, priority, mem_allocated, time_created, time_limit, time_processor, io_devices)
        process.print_processes(io_devices[0], io_devices[1], io_devices[2], io_devices[3])
        # process.offset = offset
        self.processes[process_id] = process
        return process

    # def get_process(self, id):
    #     return self.processes[id]

    # def get_processes(self):
    #     return self.processes

    # def get_id(self, process):
    #     return process.process_id

    # def delete_process(self, id):
    #     del self.processes[id]

    def get_next_process_id(self):
        self.counter += 1
        return self.counter
    
    # def num_active_processes(self):
    #     return len(self.processes)

    # def decrease_processor_times(self, id):
    #     self.processes[id].decrease_processor_time()

    # def decrease_time_limit(self, id):
    #     self.processes[id].decrease_time_limit()

    # def get_processor_time(self, id):
    #     return self.processes[id].get_processor_time()

    # def remove_finished_processes(self):
    #     for process in self.processes.values():
    #         if process.get_time_limit() == 0:
    #             self.delete_process(process.get_id())