class ArchiveManager():
    def __init__(self, memoryload: list, memory_size: int) -> None:
        self.log = []
        self.archive = {}