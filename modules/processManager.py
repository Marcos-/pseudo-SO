from modules.process import Process

'''
A classe tem métodos para criar, obter e excluir processos, bem como imprimir informações de processo. 
O método createprocess leva um dicionário de informações de processo e cria uma instância da classe 
Process do módulo modules.process. 
Em seguida, atribui à instância um ID usando o método getnextprocessid e armazena-o no dicionário self.processes, com o ID como chave. 
O método getprocess é usado para recuperar um processo do dicionário self.processes com seu ID como chave, enquanto o 
método deleteprocess é usado para excluir um processo de self.processes. 
O método printprocesses imprime informações sobre uma dada instância de processo, como seu deslocamento e prioridade. 
Por fim, getnextprocessid é usado para gerar IDs únicos para cada instância de processo criada, incrementando um contador 
interno armazenado em self.counter cada vez que é chamado.
'''

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

    def get_process(self, id):
        try:
            self.processes[id]
            return self.processes[id]
        except:
            return 0

    # def get_processes(self):
    #     return self.processes

    def print_processes(self, process):
        print("    PID:     \t", process.id)
        print("    offset:  \t", process.offset)
        print("    blocks:  \t", process.mem_allocated)
        print("    priority:\t", process.priority)
        print("    time:    \t", process.time_processor)

    # def get_id(self, process):
    #     return process.process_id

    def delete_process(self, id):
        del self.processes[id]

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