import os
from tema import file_type
import xml.etree.ElementTree as ET


class GenericFile:

    def get_path(self):
        raise NotImplementedError("Clasa GenericFile, get_path neimplementata")

    def get_freq(self):
        raise NotImplementedError("Clasa GenericFile, get_freq neimplementata")


class TextASCII(GenericFile):

    def __init__(self, path_absolut, frecvente):
        self.path_absolut = path_absolut
        self.frecvente = frecvente

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente


class TextUNICODE(GenericFile):

    def __init__(self, path_absolut, frecvente):
        self.path_absolut = path_absolut
        self.frecvente = frecvente

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente


class Binary(GenericFile):

    def __init__(self, path_absolut, frecvente):
        self.path_absolut = path_absolut
        self.frecvente = frecvente

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente


class XMLFile(TextASCII):

    first_tag = ""

    def get_first_tag(self):
        tree = ET.parse(self.path_absolut)
        root = tree.getroot()
        self.first_tag = root.tag
        return self.first_tag


class BMP(Binary):

    width = 0
    height = 0
    bpp = 0

    def show_info(self):
        return self.width, self.height, self.bpp


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
                    tip, freq = file_type(content)
                    if tip == "ASCII":
                       if content[:1].decode('utf-8') == '<':
                           xml = XMLFile(file_path, freq)
                           print(xml.get_path(), xml.get_first_tag())
                    elif tip == "UNICODE":
                        uni = TextUNICODE(file_path, freq)
                        print(f"Fisierul UNICODE: {uni.get_path}")
                    elif tip == "BINARY":
                        pass
                    else:
                        raise Exception("Tip nerecunoscut")
                finally:
                    f.close()