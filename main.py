# Authors:
#   Marcos Marques;
#   Caio Massucato;
#   Kevin Souto
#
# python main.py <input_process> <input_memory>

from kernel import Kernel
from sys import argv

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
      
   kernel = Kernel(argv[1], argv[2])

   kernel.run()
   thread = kernel.get_thread()
   thread.join()

   print("Finished")

if __name__ == "__main__":
    main()