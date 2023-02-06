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

## Requisitos
```
Python 2.7 ou 3.x
```
## Uso

Para executar o programa, basta utilizar a seguinte linha de comando:

```
python main.py <input_process> <input_archive>
```

* input_process é o arquivo de entrada que contém informações sobre os processos a serem gerenciados pelo programa. Este arquivo deve seguir um formato específico, que será detalhado em seguida. 
```Exemplo
2, 0, 3, 64, 0, 0, 0, 0
8, 0, 2, 64, 0, 0, 0, 0
```
* input_archive é o arquivo de entrada que contém informações sobre a operações de aquivo disponível para o programa. Este arquivo deve seguir um formato específico, que será detalhado em seguida.
```
10
3
X, 0, 2 Y, 3, 1
Z, 5, 3
0, 0, A, 5 0, 1, X
2, 0, B, 2 0, 0, D, 3 1, 0, E, 2
```