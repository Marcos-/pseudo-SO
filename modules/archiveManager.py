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
    
    def load_memory(self, load: list) -> None:
        for line in load:
            try: # Process operations, ex: 0, 0, A, 5
                int(line[0])
                raise Exception("Something went wrong in file sistem initialization")
            except ValueError: # File ocupation, ex: X, 0, 2
                filename = line[0]
                offset = line[1]
                filesize = line[2]
                for i in range(filesize):
                    self.archive[offset + i] = {"process_id": -1, "filename": filename, 'priority': -1}
                self.created_files[(-1, filename)] = (offset, filesize)