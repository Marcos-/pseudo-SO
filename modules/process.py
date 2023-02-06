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
    def __init__(self, id, priority, mem_allocated, time_created, time_limit, time_processor, io_devices):
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

    def run(self, time: int) -> int:
        print("process", self.id , "=>")
        print("P" + str(self.id), "STARTED")

        if (randint(0, 1) == 1):
            random_resource = randint(0, 3)
            print("P" + str(self.id), "REQUESTING", self.tasks[random_resource])
            return self.tasks[random_resource]

        sleep(time)
        return 'PROCESS_FINISHED'

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