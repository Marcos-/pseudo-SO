# pseudo-SO
Implementação de um pseudo-SO multiprogramado, composto por um Gerenciador de Processos, por um Gerenciador de Memória, por um Gerenciador de E/S e por um Gerenciador de Arquivos.

## Estrutura do Programa
O programa esta dividido em cinco grandes módulos: processo, memória, filas, recursos e arquivos:
* Módulo de Processos – classes e estruturas de dados relativas ao processo. Basicamente, mantém informações específicas do processo.
* Módulo de Filas – mantém as interfaces e funções que operam sobre os processos;
* Módulo de Memória – provê uma interface de abstração de memória RAM;
* Módulo de Recurso – trata a alocação e liberação dos recursos de E/S para os processos;
* Módulo de Arquivos – trata as operações create e delete sobre os arquivos.
