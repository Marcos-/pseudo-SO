# O pseudo-SO deve, além de escalonar o processo no compartilhamento da CPU, e gerenciar o espaço 
# de memória de acordo com as áreas reservadas, ele deve gerenciar os seguintes recursos:
# • 1 scanner
# • 2 impressoras
# • 1 modem
# • 2 dispositivos SATA
# Todos os processos, com exceção daqueles de tempo-real podem obter qualquer um desses
# recursos. O pseudo-SO deve garantir que cada recurso seja alocado para um proceso por vez. Portanto, 
# não há preempção na alocação dos dispositivos de E/S. Assim, processos de tempo-real não precisam de recursos de I/O.

'''
Esta classe é um gerenciador de recursos que é usado para escalonar processos no compartilhamento da CPU e gerenciar o espaço de memória de acordo com as áreas reservadas.
O gerenciador possui uma lista de processos prontos, um semáforo para acessar a lista, e semáforos para cada recurso (scanner, impressora, modem e dispositivos SATA).
Os métodos insertbuffer(), getbuffer(), empty_buffer() são usados para manipular a lista de processos prontos.
Os métodos requestscanner(), requestprinter(), requestmodem() e requestdisk() são usados para alocar os recursos para os processos.
O pseudo-SO garante que cada recurso seja alocado para um proceso por vez, portanto não há preempcão na alocação dos dispositivos de E/S. Processos de tempo-real não precisam de recursos de I/O.
'''

from threading import Semaphore
from time import sleep

class ResourceManager:
    def __init__(self):
        self.__ready = []
        self.buffer = Semaphore(1)
        self.scanner = Semaphore(1)
        self.printer = Semaphore(1)
        self.modem = Semaphore(1)
        self.disk = Semaphore(1)

    def insert_buffer(self, process_id, priority):
        self.buffer.acquire()
        self.__ready.append(process_id, priority)
        self.buffer.release()
    
    def get_buffer(self):
        self.buffer.acquire()
        return self.__ready

    def empty_buffer(self):
        self.__ready = []
        self.buffer.release()

    def request_scanner(self, process_id):
        self.scanner.acquire()
        print("Process acquired scanner ", process_id)
        sleep(1)
        print("Process released scanner ", process_id)
        self.scanner.release()
        return 'SUCCESS'

    def request_printer(self, process_id):
        self.printer.acquire()
        print("Process acquired printer ", process_id)
        sleep(1)
        print("Process released printer ", process_id)
        self.printer.release()
        return 'SUCCESS'
    
    def request_modem(self, process_id):
        self.modem.acquire()
        print("Process acquired modem ", process_id)
        sleep(1)
        print("Process released modem ", process_id)
        self.modem.release()
        return 'SUCCESS'

    def request_disk(self, process_id):
        self.disk.acquire()
        print("Process acquired disk ", process_id)
        sleep(1)
        print("Process released disk ", process_id)
        self.disk.release()
        return 'SUCCESS'

