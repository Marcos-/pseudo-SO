# Authors:
#   Marcos Marques;
#   Caio Massucato;
#   Kevin Souto
#
# python main.py <input_process> <input_memory>

from kernel import Kernel
from sys import argv
from utils.readProcess import read_processes
from utils.readArchive import read_archive

def main():
   try:
      argv[1]
      argv[2]
      # if len(argv) == 0:
      #    print("usage: python main.py <input_process> <input_memory>")
      #    return
   except:
      print("usage: python main.py <input_process> <input_memory>")
      return 0

   # Read inputs from files
   processes = read_processes(argv[1])
   archives = read_archive(argv[2])
      
   kernel = Kernel(processes, archives)

   # kernel.run()
   # thread = kernel.get_thread()
   # thread.join()

   print("Finished")

if __name__ == "__main__":
    main()