# PARSER

import re
from util import *
from handlers import *
from rules import *


class Parser:

    def __init__(self, handler):
        self.filters = []
        self.rules = []
        self.handler = handler

    def addFilter(self, pattern, name):
        def regexsub(line, handler):
            return re.sub(pattern, handler.sub(name), line)
        self.filters.append(regexsub)

    def addRule(self, rule):
        self.rules.append(rule)

    def parse(self, file, file2):
        self.handler.start('html', file2)
        for line in blocks(file):
            for filter in self.filters:
                line = filter(line, self.handler)
            for rule in self.rules:
                if rule.condition(line):
                    if rule.action(line, file2, self.handler):
                        break
        self.handler.end('html', file2)


class BasicTextParser(Parser):
    def __init__(self, handler):

        Parser.__init__(self, handler)

        self.addFilter(r'[*](.*)[*]', 'emphasize')
        self.addFilter(r'\((https?:\S+)\)', 'weblink')
        self.addFilter(r'([A-Z][A-Z]+)', 'allCapital')
        self.addFilter(r'\((\w+@\w+\.[a-z]+)\)', 'email')

        self.addRule(ListItemRule())
        self.addRule(ListRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())



handler = HTMLRenderer()
parser = BasicTextParser(handler)
with open('test_input.txt') as file:
    with open('test_output.html', mode='w') as file2:
        parser.parse(file, file2)
