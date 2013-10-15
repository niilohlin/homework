#!/usr/bin/env python
# -*- coding: utf-8 -*-

import parser

class Entry:
    def __init__(self, name, number):
        self.aliaslist = []
        self.aliaslist.append(name)
        self.number = number
    
    def alias(self, alias):
        self.aliaslist.append(alias)
    
    def change(self, newnumber):
        self.number = newnumber

def get(pbook, name):
    for entry in pbook:
        for alias in entry.aliaslist:
            if name == alias:
                return entry
    

def add(pbook, name, number):
    pbook.append(Entry(name, number))

def alias(pbook, name, newname):
    get(pbook, name).alias(newname)

def lookup(pbook, name):
    temp = get(pbook, name)
    if not temp == None:
        return "%s has phonenumber %s" %(name, temp.number)
    else:
        return "%s not in phonebook" % name
    
def exe(pbook, tree):
    
    succ = True
    res = ""
    for statement in tree:
        if statement[0] == parser.Keyword("add"):
            add(pbook, statement[1], statement[2])
        elif statement[0] == parser.Keyword("alias"):
            alias(pbook, statement[1], statement[2])
        elif statement[0] == parser.Keyword("lookup"):
            res = lookup(pbook, statement[1])
            
        if not res == '':
            print res
            res = ''
           
prompt = "phonebook"
def main():
    pbook = []
    while True:
        print prompt,
        try:
            a = raw_input()
            print a
        except:
            break
        succ, tree = parser.parse(parser.lexer(a))
        exe(pbook, tree)

if __name__ == '__main__':
    main()
