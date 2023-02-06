# A alocação de memória deve ser implementada como um conjunto de blocos contíguos, onde cada bloco equivale uma palavra da memória real.
# Cada processo deve alocar um segmento contíguo de memória, o qual permanecerá alocado durante toda a execução do processo. Deve-se notar 
# que não é necessário a implementação de memória virtual, swap, nem sistema de paginação. Portanto, não é necessário gerenciar a memória, 
# apenas verificar a disponibilidade de recursos antes de iniciar um processo.
# Deve ser utilizado um tamanho fixo de memória de 1024 blocos. Dessa quantidade, 64 blocos devem ser reservados para processos de 
# tempo-real e os 960 blocos restantes devem ser compartilhados entre os processos de usuário. A Figura 2 ilustra o caso onde cada 
# bloco de memória possui 1 MB.

class MemoryManager:
    def __init__(self, memory_size):
        self.memory_size = memory_size
        self.allocations = {}
        self.offset = 0

    def load(self, process_id, size, offset):
        if self.offset + size > self.memory_size:
            return 'NOT_ENOUGH_RAM_MEMORY'
        self.allocations[process_id] = (self.offset, size)
        offset[0] = self.offset
        self.offset += size
        return 'SUCCESS'
    

