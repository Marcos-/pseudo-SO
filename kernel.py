from datetime import datetime
from time import sleep
from threading import Thread

from modules.processManager import ProcessManager
from modules.memoryManager import MemoryManager
from modules.queueManager import QueueManager
from modules.resourceManager import ResourceManager

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

        self.active_processes = []
        self.num_processes = 0

        self.process_manager = ProcessManager()
        self.memory_manager = MemoryManager(1024)
        self.queue_manager = QueueManager(1)
        self.resource_manager = ResourceManager()

        self.quantum = 1
        self.start_time = datetime.now()

        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        for process in self.input_process:
            self.process_manager.create_process(process)
            # self.memory_manager.insert_process(process)
        while True:
            self.run_processes()
            sleep(1)
    
    def run_processes(self):

        for process in self.process_manager.get_processes():
            print(process.get_id(), process.get_processor_time(), process.get_time_limit())
            process.decrease_processor_time()
            process.decrease_time_limit()

            if process.get_processor_time() == 0:
                self.queue_manager.insert_process(process.get_priority(), process)
                process.set_processor_time(2)
        
        self.process_manager.remove_finished_processes()
