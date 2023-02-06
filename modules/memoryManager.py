# A alocação de memória deve ser implementada como um conjunto de blocos contíguos, onde cada bloco equivale uma palavra da memória real.
# Cada processo deve alocar um segmento contíguo de memória, o qual permanecerá alocado durante toda a execução do processo. Deve-se notar 
# que não é necessário a implementação de memória virtual, swap, nem sistema de paginação. Portanto, não é necessário gerenciar a memória, 
# apenas verificar a disponibilidade de recursos antes de iniciar um processo.
# Deve ser utilizado um tamanho fixo de memória de 1024 blocos. Dessa quantidade, 64 blocos devem ser reservados para processos de 
# tempo-real e os 960 blocos restantes devem ser compartilhados entre os processos de usuário. A Figura 2 ilustra o caso onde cada 
# bloco de memória possui 1 MB.

A = 1
NA = 0

class MemoryManager:
    def __init__(self, memory_size):
        self.memory_size = memory_size
        self.allocations = {}
        self.offset = 0
        self.memory_blocks = [A] * memory_size # A(1): livre; NA(0): ocupado

    def load(self, process_id, size, offset):
        free_mem = {}
        mem_index = 0
        block_size = 0

        while(mem_index < len(self.memory_blocks)):
            if (self.memory_blocks[mem_index] == A and block_size < size):
                block_size +=1
            else:
                if(block_size >= size):
                    free_mem[mem_index - block_size] = block_size
                    break
                block_size = 0
            mem_index +=1

        if self.offset + size > free_mem[mem_index - block_size]:
            return 'NOT_ENOUGH_RAM_MEMORY'
        
        while(block_size >= 0):
            self.memory_blocks[block_size] = NA
            block_size -= 1

        self.allocations[process_id] = (self.offset, size)
        offset[0] = self.offset
        # self.offset += size
        return 'SUCCESS'

    def unload(self, process_id, size, offset):
        while(size>=0):
            self.memory_blocks[offset + size - 1] = NA
            size -= 1
        self.allocations.pop(process_id)

