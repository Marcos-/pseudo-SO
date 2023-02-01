from datetime import datetime
from time import sleep
from threading import Thread

from modules.processManager import ProcessManager


class Kernel:
    def __init__(self, input_process, input_memory):
        self.input_process = input_process
        self.input_memory = input_memory
        self.process_manager = ProcessManager()
        # self.memory_manager = MemoryManager(1024)
        # self.queue_manager = QueueManager(1)
        # self.resource_manager = ResourceManager()
        self.processes = []
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        # self.load_processes()
        # self.load_memory()
        self.run_processes()

    # def load_processes(self):
    #     self.processes = archives.load_processes(self.input_process)

    # def load_memory(self):
    #     for process in self.processes:
    #         self.memory_manager.load(process.id, process.mem_allocated, process.offset)

    def run_processes(self):
        while self.process_manager.num_active_processes() > 0:
            self.queue_manager.aging()
            process_id = self.queue_manager.next_process()
            if process_id == NO_NEXT_PROCESS:
                continue
            process = self.process_manager.get_process(process_id)
            if process.time_limit == 0:
                self.process_manager.delete_process(process.id)
                self.memory_manager.remove(process.id, process.mem_allocated, process.offset)
                continue
            process.time_limit -= 1
            process.time_processor -= 1
            if process.time_processor == 0:
                self.queue_manager.insert(process.id, process.priority)
                process.time_processor = 2
            sleep(1)

    def get_thread(self):
        return self.thread
