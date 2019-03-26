#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import logging
from logging.config import fileConfig
from pathlib import Path
from snippet import VSCodeFile

def ParseUltiSnip(snipFile):
    with open (snipFile, mode='r') as ultiF:
        for line in ultiF:
            if line.startswith('snippet'):
                print(line.strip('snippet '))
                print(line)
    ultiF.close()


def main():
    fileConfig('logging_config.ini')
    logging.getLogger(__name__).addHandler(logging.NullHandler())
    logger = logging.getLogger()
    logger = logging.getLogger('SnipSwitch')
    logging.debug("Hit main.")
    home = str(Path.home())
    ParseUltiSnip(f"{home}/Dropbox/dotfiles/vim/.vim/ultisnips-shm/markdown.snippets")
    vsc = VSCodeFile("", "test")
    vsc.create_snippet_file()

if __name__ == '__main__':
    main()
