from modules.archiveManager import ArchiveManager
from modules.resourceManager import ResourceManager
from datetime import datetime
from random import randint
from time import sleep

'''
A classe Process é usada para criar objetos que representam processos.
Ele tem atributos como id, prioridade, memallocated, timecreated, timelimit, timeprocessor e io_devices.
Ele também tem métodos como run() e print_processes(). O método run() recebe um parâmetro de tempo e retorna uma string dependendo do número aleatório gerado.
O método print_processes() imprime os atributos do objeto processo.
A classe importa módulos de outros arquivos como ArchiveManager, ResourceManager, datetime, random e time.
'''

class Process:
    def __init__(self, id, priority, mem_allocated, time_created, time_limit, time_processor, io_devices, archive):
        self.id = id
        self.priority = priority
        self.mem_allocated = mem_allocated
        self.time_created = time_created
        self.time_limit = time_limit
        self.time_processor = time_processor
        self.io_devices = io_devices
        self.offset = 0
        self.mem_allocated = mem_allocated
        self.instruction_counter = 1
        self.tasks = [
            'PRINT',
            'SCAN',
            'MODEM',
            'DISK'
        ]
        self.archive = archive
        self.archive_tasks = []
        self.archive_ops(archive[3])

    def run(self, time: int) -> int:
        print("process", self.id , "=>")
        print("P" + str(self.id), "STARTED")

        if(len(self.archive_tasks) > 0):
            task = self.archive_tasks.pop(randint(0, 100) % len(self.archive_tasks))
            # If needs some archive operation, let the archive module handle
            if task[0] == 'ARCHIVE_ACTION':
                op = task[1]
                print("Task: ",op)
                print("Operation: ",op[1])
                print("Name: ", op[2])
                print("Priority: ",self.priority)
                if op[1] == 0:
                    ArchiveManager.createfile(processID=self.id, filename=op[2], filesize=op[3], priority=self.priority)
                # elif op[1] == 1:
                #     ArchiveManager.deletefile(self.id, op[2], self.priority)

        if (randint(0, 1) == 1):
            random_resource = randint(0, 3)
            print("P" + str(self.id), "REQUESTING", self.tasks[random_resource])
            return self.tasks[random_resource]

        sleep(time)
        return 'PROCESS_FINISHED'
    
    def archive_ops(self, ops):
        if len(ops) > 0:
            [self.archive_tasks.append(['ARCHIVE_ACTION', ops.pop(0)]) for _ in range(len(ops))]
        print("Tasks: ",self.archive_tasks)

    def print_processes(self, printer, scanner, modem, driver):
        print("    PID:     \t", self.id)
        print("    offset:  \t", self.offset)
        print("    blocks:  \t", self.mem_allocated)
        print("    priority:\t", self.priority)
        print("    time:    \t", self.time_processor)
        print("    printers:\t", printer)
        print("    canners: \t", scanner)
        print("    modems:  \t", modem)
        print("    drives:  \t", driver, "\n")