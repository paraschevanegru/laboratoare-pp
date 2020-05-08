import argparse
import subprocess
import shlex


def functie():
    parser = argparse.ArgumentParser(description='Process command')
    parser.add_argument('command', metavar='cmd', nargs='+',
                        help='an integer for the accumulator')
    args = parser.parse_args()
    cmd = args.command[0].split('|')
    print(cmd)
    print(run(cmd))


def run(command_list):
    process_list = list()
    previous_process = None
    for command in command_list:
        args = shlex.split(command)
        if previous_process is None:
            process = subprocess.Popen(args, stdout=subprocess.PIPE)
        else:
            process = subprocess.Popen(args,
                                        stdin=previous_process.stdout,
                                        stdout=subprocess.PIPE)
        process_list.append(process)
        previous_process = process
    last_process = process_list[-1]
    output, _ = last_process.communicate()
    return output.decode("utf-8")

if __name__ == '__main__':
    functie()
    