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
            wait = int(process['init_time']) - (datetime.now() - self.start_time).microseconds / 1000000
            print("Process {} will start in {} seconds".format(process, wait))
            sleep(wait)

            offset = [0]
            if self.memory_manager.load(process['id'], process['memory_blocks'], offset) != 'NOT_ENOUGH_RAM_MEMORY':
                self.process_manager.create_process(process, self.input_archive)
                self.queue_manager.insert(process['id'], process['priority'])
                self.num_processes += 1
            else:
                print("Error: Not enough RAM memory")
                break

    def scheduler(self):
        while self.num_processes > 0:

            for (id, priority) in self.resource_manager.get_buffer():
                self.queue_manager.insert(id, priority)
            
            self.resource_manager.empty_buffer()

            self.queue_manager.aging()

            # Check which is the next process to be run, if there is a process it must be removed from queue
            id = self.queue_manager.next_process()

            print("Next process: {}".format(id))
            # If there is next process
            if id != 'NO_NEXT_PROCESS':
                # Get instance of Process
                process = self.process_manager.get_process(id)

                self.process_manager.print_processes(process)

                # Execute till the end if is a real time process, else, execute a quantum
                if process.priority == 0:
                    duration = process.time_processor
                else:
                    duration = self.quantum
                code = process.run(duration)
                
                # If the process has finished, so it has to free the memory occupied by the process
                if code == 'PROCESS_FINISHED':
                    self.memory_manager.remove(id, process.mem_allocated, process.offset)
                    self.process_manager.delete_process(id)
                    self.num_processes -= 1
                    print("Process {} finished".format(id))
                else:
                    resource_thread = Thread(target=self.resource_request, args=(code, id, process.priority))
                    resource_thread.start()
                    self.queue_manager.insert(id, process.priority)

    def resource_request(self, code, id, priority):
        if code == 'PRINTER':
            self.resource_manager.request_printer(id)
        elif code == 'SCANNER':
            self.resource_manager.request_scanner(id)
        elif code == 'MODEM':
            self.resource_manager.request_modem(id)
        elif code == 'DISK':
            self.resource_manager.request_disk(id)
        
