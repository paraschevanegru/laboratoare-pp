import argparse
import subprocess
import shlex


def functie():
    parser = argparse.ArgumentParser(description='Process command')
    parser.add_argument('command', metavar='cmd', nargs='+',
                        help='a command in quotes')
    args = parser.parse_args()
    # pune comenzile separat intr-o lista
    cmd = args.command[0].split('|')  
    print(cmd)
    # executia la comada
    print(run(cmd))  


def run(command_list):
    process_list = list()
    previous_process = None
    for command in command_list:
         # shlex.split imparte un string cu acele comenzi intr-o lista
        args = shlex.split(command) 
        if previous_process is None:
            # daca nu exista un proces anterior pune in stdout rezultatul executiei comenzii
            process = subprocess.Popen(args, stdout=subprocess.PIPE)  
        else:
            process = subprocess.Popen(args,
                                        stdin=previous_process.stdout,
                                        stdout=subprocess.PIPE)
        # creeaza lista de procese                              
        process_list.append(process)
        previous_process = process
    # ia ultimul proces din lista
    last_process = process_list[-1]
    # citim output-ul de la acest proces si ignoram erorile
    output, _ = last_process.communicate()
    # facem decode la byte output
    return output.decode("utf-8")

if __name__ == '__main__':
    # un exemplu de rulare in linia de comanda ar fi: python lab11-p2.py "ls -la | grep lab11"
    functie()
    