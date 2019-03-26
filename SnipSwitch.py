#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import logging
from logging.config import fileConfig

def main():
    fileConfig('logging_config.ini')
    logging.getLogger(__name__).addHandler(logging.NullHandler())
    logger = logging.getLogger()
    logger = logging.getLogger('SnipSwitch')
    logging.debug("Hit main.")

if __name__ == '__main__':
    main()
