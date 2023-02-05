# pseudo-SO
Implementação de um pseudo-SO multiprogramado, composto por um Gerenciador de Processos, por um Gerenciador de Memória, por um Gerenciador de E/S e por um Gerenciador de Arquivos.

## Estrutura do Programa
O programa esta dividido em cinco grandes módulos: processo, memória, filas, recursos e arquivos:
* Módulo de Processos – classes e estruturas de dados relativas ao processo. Basicamente, mantém informações específicas do processo.
* Módulo de Filas – mantém as interfaces e funções que operam sobre os processos;
* Módulo de Memória – provê uma interface de abstração de memória RAM;
* Módulo de Recurso – trata a alocação e liberação dos recursos de E/S para os processos;
* Módulo de Arquivos – trata as operações create e delete sobre os arquivos.

### Gerente de Processo:
Crie processos e gerencie sua execução, agendamento e finalização.
Você pode usar o módulo de multiprocessamento em Python para criar processos e gerenciar sua execução.
### Gerenciador de memória:
Alocar e desalocar memória dinamicamente para processos.
A implementação de um gerenciador de memória exigiria um bom entendimento dos conceitos de gerenciamento de memória, como paginação e segmentação.
### Gerenciador de E/S:
Gerenciar operações de entrada e saída para os processos.
Você pode usar o módulo io em Python para executar operações de entrada e saída.
### Gerenciador de arquivos:
Gerencie o sistema de arquivos e as operações de arquivo, como criação, leitura, gravação e exclusão de arquivos.
Você pode usar o módulo os em Python para executar operações de arquivo e gerenciar o sistema de arquivos.
