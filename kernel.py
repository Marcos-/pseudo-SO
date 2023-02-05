from datetime import datetime
from time import sleep
from threading import Thread

from modules.processManager import ProcessManager
from modules.memoryManager import MemoryManager

'''
A classe Kernel é usada para gerenciar processos, memória e filas. O construtor inicializa o gerenciador de processos e 
cria um thread que executará o método run(). O método run() chama o método run_processes() que percorre cada processo ativo e diminui seu limite de 
tempo e processador de tempo. Se o processador de tempo chegar a 0, ele insere o processo em uma fila com sua prioridade e define o processador de 
tempo de volta para 2. Finalmente, ele dorme por 1 segundo antes de percorrer o próximo processo.
'''

class Kernel:
    def __init__(self, input_process, input_archive):
        self.input_process = input_process
        self.input_archive = input_archive
        self.process_manager = ProcessManager()
        self.memory_manager = MemoryManager(1024)
        # self.queue_manager = QueueManager(1)
        # self.resource_manager = ResourceManager()
        self.processes = []
        self.thread = Thread(target=self.run)
        self.thread.start()
        self.start_time = datetime.now()

    def run(self):
        # self.load_processes()
        self.load_memory()
        self.run_processes()
        print(self)

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

    def load_memory(self):
        for process in self.processes:
            self.memory_manager.load(process.id, process.mem_allocated, process.offset)

    def scheduler(self):
        
