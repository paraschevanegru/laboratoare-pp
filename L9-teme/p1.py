from abc import ABC, abstractmethod
from typing import Any, Optional, Tuple, List
from pathlib import Path
import re
import subprocess
import argparse


class Handler(ABC):


    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self,request) -> Optional[str]:
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None


    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler


    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class KotlinHandler(AbstractHandler):

    exp = ["val", "var", "fun", "$", "when", "true", "Boolean", "println", "String", 
           "Array", "readText", "forEach", "throw"]
    delit = ["(",")","{","}", ".", "<", ">", " ", ":", "\n"]
    shebang = ["#!/usr/bin/env kotlinc -script"]
    def handle(self, request: Any) -> str:
        file_path, shebang, _, freq = procesare_fisier(request, self.exp, self.delit)
        comp = (freq[0] * len(self.exp)) / 100
        if shebang in self.shebang:
            print("kotlin")
            subprocess.Popen(f'mv {file_path} {file_path}.kt; kotlinc kotfile.kt -include-runtime -d kotfile.jar  {file_path}.; java kotfile.jar', shell=True)
        elif comp >= 0.5:
            print("kotlin")
            subprocess.Popen(f'mv {file_path} {file_path}.kt; kotlinc kotfile.kt -include-runtime -d kotfile.jar  {file_path}.; java kotfile.jar', shell=True)
        else:
            return super().handle(request)


class PythonHandler(AbstractHandler):

    exp = ["def","self","pass", "async", "elif", "str", "from", "__name__", "__main__", "else:", 
           "None", "await", "break", "continue", "True", "False", "yield", "raise", 
           "assert", "not", "except", "end"]
    delit = ["(",")", ".", '"']
    shebang = ["#!/usr/bin/env python3", "#!/usr/bin/env python"]
    def handle(self, request: Any) -> str:
        file_path, shebang, _, freq = procesare_fisier(request, self.exp, self.delit)
        comp = (freq[0] * len(self.exp)) / 100
        if shebang in self.shebang:
            print("python")
            subprocess.Popen(f'python {file_path}', shell=True)
        elif comp >= 0.5:
            print("python")
            subprocess.Popen(f'python {file_path}', shell=True)
        else:
            return super().handle(request)

class BashHandeler(AbstractHandler):

    exp = ["echo", "done", "read", "function", "until", "select", "fi", "elif", "case", "do",
           "else", "esac", "then"]
    delit = ["(",")","{","}", ".", '"']
    shebang = ["#!/usr/bin/env bash", "#!/bin/bash", "#!/bin/sh", "#!/bin/sh -"]
    def handle(self, request: Any) -> str:
        file_path, shebang, _, freq = procesare_fisier(request, self.exp, self.delit)
        comp = (freq[0] * len(self.exp)) / 100
        if shebang in self.shebang:
            print("bash")
            subprocess.Popen(f'./{file_path}', shell=True)
        elif comp >= 0.5:
            print("bash")
            subprocess.Popen(f'./{file_path}', shell=True)
        else:
            return super().handle(request)


class JavaHandler(AbstractHandler):

    exp = ["System", "public", "static", "catch", "try", "this", "private", "protected", 
           "throws", "new", "class", "default"]
    delit = ["(",")","{","}", "."]
    shebang = ["#!/opt/java/jdk-8/bin/java --source 8", "#!/opt/java/jdk-11/bin/java --source 11", 
               "#!/opt/java/jdk-13/bin/java --source 13", "#!/opt/java/jdk-14/bin/java --source 14"]
    def handle(self, request: Any) -> str:
        file_path, shebang, _, freq = procesare_fisier(request, self.exp, self.delit)
        comp = (freq[0] * len(self.exp)) / 100
        if shebang in self.shebang:
            print("java")
            subprocess.Popen(f'cp {file_path} {file_path}.java; javac {file_path}.java; java Main', shell=True)
        elif comp >= 0.5:
            print("java")
            subprocess.Popen(f'cp {file_path} {file_path}.java; javac {file_path}.java; java Main', shell=True)
        else:
            return super().handle(request)


def procesare_fisier(file_path: str, keywords: List, delimitatori: List) -> Tuple:

    frequency = [0, 0]
    words = set()
    first_line = ""
    regexPattern = '|'.join(map(re.escape, delimitatori))

    with open(file_path,"r") as fisier: 
        first_line = fisier.readline()
        fisier.seek(0)
        txt = fisier.read()
        for i in keywords:
            if re.search(r'\b{}\b'.format(i), txt):
                frequency[0] += 1
        fisier.seek(0)
        for line in fisier:         
            for word in re.split(regexPattern, line):           
                words.add(word)
                frequency[1] += 1 

    return file_path, first_line.rstrip(), words, frequency


def procesare_rezultat(handler: Handler, fisier: str) -> None:

    handler.handle(fisier)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process command')
    parser.add_argument('fisier', help='path fisier relativ la director sau path absolut')
    args = parser.parse_args()
    fis = args.fisier
    kot = KotlinHandler()
    pyt = PythonHandler()
    bsh = BashHandeler()
    jav = JavaHandler()
    kot.set_next(pyt).set_next(bsh).set_next(jav)

    p = Path(fis)
    procesare_rezultat(kot, p)

