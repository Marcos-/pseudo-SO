def run_process(data):
  # extrair os dados de cada linha
  init_time, priority, processor_time, memory_blocks, printer_code, scanner, modem, disk_code = data.split(',')

  return init_time, priority, processor_time, memory_blocks, printer_code, scanner, modem, disk_code

def printProcess(process):
    init_time, priority, processor_time, memory_blocks, printer_code, scanner, modem, disk_code = process
    print("Processo iniciado com os seguintes dados:")
    print("Tempo de inicialização:", init_time)
    print("Prioridade:", priority)
    print("Tempo de processador:", processor_time)
    print("Blocos em memória:", memory_blocks)
    print("Número-código da impressora requisitada:", printer_code)
    print("Requisição do scanner:", scanner)
    print("Requisição do modem:", modem)
    print("Número-código do disco:", disk_code)

def read_processes(filename):
  with open(filename, 'r') as file:
    # ler as linhas do arquivo
    data = file.readlines()

    # criar uma lista de processos
    processes = []
    for line in data:
      process = run_process(line,)
      processes.append(process)
      printProcess(process)

    return processes

# ler o arquivo 'processes.txt' e iniciar os processos
if __name__ == '__main__':
  start_processes('input/processes.txt')
