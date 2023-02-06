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
        self.queue_manager = QueueManager(10)
        self.resource_manager = ResourceManager()

        self.quantum = 1
        self.start_time = datetime.now()

        self.thread = Thread(target=self.run)
        self.thread2 = Thread(target=self.scheduler)

        self.thread.start()
        self.thread.join()

        self.thread2.start()
        self.thread2.join()

    def run(self):
        print("Running kernel")
        for process in self.input_process:
            wait = int(process['init_time']) - (datetime.now() - self.start_time).microseconds / 10000
            print("Process {} will start in {} seconds".format(process, wait))
            sleep(wait)

            offset = [0]
            if self.memory_manager.load(process['id'], process['memory_blocks'], offset) != 'NOT_ENOUGH_RAM_MEMORY':
                self.process_manager.create_process(process)
                self.queue_manager.insert(process['id'], process['priority'])
                self.num_processes += 1
            else:
                print("Not enough RAM memory")
                break

    def scheduler(self):
        while self.num_processes > 0:

            for (id, priority) in self.resource_manager.get_buffer():
                self.queue_manager.insert(id, priority)
            
            self.resource_manager.empty_buffer()

            self.queue_manager.aging()