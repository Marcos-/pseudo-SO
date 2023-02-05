def read_archive(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        quantity_blocks = int(lines[0])
        quantity_segments = int(lines[1])

        files = {}
        for i in range(2, quantity_segments + 2):
            file_data = lines[i].replace(',', '').split()
            file_name = file_data[0]
            first_block = int(file_data[1])
            number_of_occupied_blocks = int(file_data[2])
            files[file_name] = (first_block, number_of_occupied_blocks)

        operations = []
        for i in range(quantity_segments + 2, len(lines)):
            operation_data = lines[i].replace(',', '').split()
            process_id = int(operation_data[0]) 
            operation_code = int(operation_data[1]) 
            file_name = operation_data[2] 
            if operation_code == 0: 
                number_of_blocks= int(operation_data[3]) 
                operations.append((process_id, operation_code, file_name, number_of_blocks)) 
            else: 
                operations.append((process_id, operation_code, file_name))

        return quantity_blocks, quantity_segments, files, operations

if __name__ == '__main__':
    quantity_blocks, quantity_segments, files, operations = read_archive('input/filex.txt')
    print("Quantity of blocks:", quantity_blocks)
    print("Quantity of segments occupied:", quantity_segments)
    print("Files:", files)
    print("Operations:", operations)