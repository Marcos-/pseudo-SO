class ArchiveManager():
    def __init__(self, memoryload: list, memory_size: int) -> None:
        self.log = []
        self.archive = {}
        self.created_files = {}

    def createfile(self, processID: int, filename: str, filesize: int, priority: int) -> int:
        filesize = int(filesize)
        print("** Process", processID, " creating a file named", filename, "\n")
        # Check if the file name and user already exists
        keys = self.created_files.keys()
        if (processID, filename) in keys or (-1, filename) in keys:
            return self.register_operation(processID, filename, 'CREATE_FILE_NAME_IN_USE', offset= (-1), filesize=filesize)
        
        # Iterate over all memory to check the first contiguous space to store a new file
        i: int = 0
        count = 0  
        while(i < len(self.archive)):
            if (self.archive[i] != {}):
                if(count >= filesize):
                    self.__alocate(filename, filesize, processID, (i-count), priority)
                    self.created_files[(processID, filename)] = (i-count, filesize)
                    return self.register_operation(processID, filename, 'CREATE_FILE_SUCESS', offset= (i-count), filesize=filesize)
                count = 0
            else:
                count+=1
            i+=1
        if(count >= filesize):
            self.__alocate(filename, filesize, processID, (i-count), priority)
            self.created_files[(processID, filename)] = (i-count, filesize)
            return self.register_operation(processID, filename, 'CREATE_FILE_SUCESS', offset= (i-count), filesize=filesize)
        return self.register_operation(processID, filename, 'CREATE_FILE_NOT_ENOUGTH_MEM')


    def register_operation(self, processID: int, filename: str, operationID: int, offset: int = 0, filesize: int = 0) -> int:
        self.log.append({"process_id": processID, "operation": operationID, "filename": filename, "offset": offset, "filesize": filesize});
        return operationID

    def __alocate(self, filename: str, size: int, processId: int, offset: int, priority: int) -> None:
        while(size>0):
            self.archive[offset + size - 1] = {"process_id": processId, "filename": filename, "priority": priority}
            size -= 1
    
    def parseOperation(self, operationID: int):
        if(operationID == 'CREATE_FILE_SUCESS'):
            return {"status": True, "operation": 0,"reason": ""}
        elif(operationID == 'CREATE_FILE_NOT_ENOUGTH_MEM'):
            return {"status": False, "operation": 0, "reason": "Memória insuficiente"}
        elif(operationID == 'CREATE_FILE_NAME_IN_USE'):   
            return {"status": False, "operation": 0, "reason": "Arquivo já existe"}     
        elif(operationID == 'DELETE_FILE_SUCESS'):
            return {"status": True, "operation": 1, "reason": ""}
        elif(operationID == 'DELETE_FILE_NOT_PERMITTED'):
            return {"status": False, "operation": 1, "reason": "Acesso negado"}        
        elif(operationID == 'FILE_NOT_FOUND'):   
            return {"status": False, "operation": 1, "reason": "Arquivo nao encontrado"} 
        elif(operationID == 'INVALID_PROCESS_ID'):   
            return {"status": False, "operation": 1, "reason": "O processo não existe"}
    
    def print_file_log(self) -> None:
        print("Sistema de arquivos =>")
        for i in range(len(self.log)):
            log = self.log[i]
            parsed_operation = self.parseOperation(log["operation"])
            operation = parsed_operation["operation"]
            status = parsed_operation["status"]
            print("Operação {index} => {status}"
                .format(
                    index = i+1, 
                    status = ( "Sucesso" if status else "Falha")
                )
            )
            print("O processo {process}{status_identifier} o arquivo {file}. {reason}"
                .format(
                    process = log["process_id"], 
                    status_identifier = " {op}".format(op="criou" if operation == 0 else "deletou") if status else " não pode {op}".format(op="criar" if operation == 0 else "deletar"),
                    file = log["filename"],
                    reason = parsed_operation["reason"] if parsed_operation["reason"] != "" else "Blocos: {start} .. {end}".format(start=log["offset"], end=log["offset"]+log["filesize"]-1 )
                )
            )
            print("")