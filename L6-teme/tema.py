import os
import struct

def file_type(content):
    # frecvente
    # frequency_list[0] reprezinta nr zerouri
    # frequency_list[1] reprezinta limita [9, 10, 13, 32...127]
    # frequency_list[2] reprezinta limita [1..8, 11, 12,15.. 31,127..255]
    frequency_list = [0, 0, 0]

    # for line in fileContent:
    for char in content:
        if char == 0:
            frequency_list[0] += 1
        elif (char in [9, 10, 13]) or (32 <= char <= 127):
            frequency_list[1] += 1
        else:
            frequency_list[2] += 1
    total_char = sum(frequency_list)

    # Trebuie determinat cat la % reprezinta fiecare lista de caractere
    if frequency_list[2] == 0 and frequency_list[0] == 0:
        x = 0
    else:
        x = (100 * (frequency_list[2] + frequency_list[0])) / total_char
    if frequency_list[1] == 0:
        y = 0
    else:
        y = (100 * frequency_list[1]) / total_char
    tip = ""
    if x < y:
        tip = "ASCII"
    elif 3 / 10 * total_char <= frequency_list[0]:
        tip = "UNICODE"
    else:
      tip = "BINARY"
    
    return tip, frequency_list


if __name__ == '__main__':
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    for root, subdirs, files in os.walk(ROOT_DIR):
        for file in os.listdir(root):
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                # deschide fișierul spre acces binar
                f = open(file_path, 'rb')
                try:
                    # în content se va depune o listă de octeți
                    content = f.read()
                    # semnifactia "_" este de a ignora acel elem de la return
                    tip, _ = file_type(content)
                    # folosim f-string
                    print(f"Fisierul {file_path} este de tipul: {tip}")
                finally:
                    f.close()