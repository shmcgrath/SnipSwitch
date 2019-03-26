#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import logging
from logging.config import fileConfig

class Snippet:
    def __init__(self, trigger):
        # text that will trigger snippet after tab
        self.trigger = trigger #prefix in vs code
        # body is list of strings in vscode
        # in vsc replace tab from ultisnip with \t and vice versa
        # expanded and inserted into code
        self.body = None
        self.description = None
        self.options = None #UltiSnips individual letters
        # scope is for global snippets in vs code Languages in vs code
        # dds of the langs where the snippet is applicable in the scope field
        # "javascript,typescript"
        # empty or omitted, the snippet gets applied to all languages
        self.scope = None
        self.name = None

class SnippetFile:
    editor = None
    ext = None
    format = None
    header = None
    footer = None
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename

    def create_snippet_file(self):
        #TODO: check if path ends with / or not
        file = self.path + self.filename + self.ext
        print(file)
        self.create_snippet_header(file)
        self.create_snippet_footer(file)

    def create_snippet_header(self, file):
        with open (file, mode='w') as newSnip: 
            newSnip.write("")
            if self.header is not None:
                newSnip.write(self.header)
            newSnip.close()

    def create_snippet_footer(self, file):
        if self.footer is not None:
            with open (file, mode='a') as newSnip: 
                newSnip.write("\n" + self.footer)
                newSnip.close()

class VSCodeFile(SnippetFile):
    editor = "Visual Studio Code"
    ext = ".code-snippets"
    format = "json"
    header = "{"
    footer = "}"
    def __init__(self, path, file):
        super().__init__(path, file)

class UltiSnips(SnippetFile):
    editor = "Vim"
    ext = ".snippets"
    format = "UltiSnips"
    header = None
    footer = None
    def __init__(self, path, file):
        super().__init__(path, file)
