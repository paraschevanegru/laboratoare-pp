import os


class GenericFile:

    def get_path(self):
        raise NotImplementedError("Clasa GenericFile, get_path neimplementata")

    def get_freq(self):
        raise NotImplementedError("Clasa GenericFile, get_freq neimplementata")


class TextASCII(GenericFile):

    path_absolut = ""
    frecvente = ""

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente


class TextUNICODE(GenericFile):

    path_absolut = ""
    frecvente = ""

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente


class Binary(GenericFile):

    path_absolut = ""
    frecvente = ""

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente


class XMLFile(TextASCII):

    first_tag = ""

    def get_first_tag(self):
        return self.first_tag


class f(Binary):

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
            print(file_path)
            if os.path.isfile(file_path):
                # deschide fișierul spre acces binar
                f = open(file_path, 'rb')
                try:
                    # în content se va depune o listă de octeți
                    content = f.read()
                finally:
                    f.close()