#!/usr/bin/env python
# -*- coding: utf-8 -*-

import parser
import sys

class Entry:
    """Entry, name + number where name and number is a string"""
    def __init__(self, name, number):
        self.aliaslist = [name]
        self.number = number
    
    def alias(self, alias):
        self.aliaslist.append(alias)
    
    def change(self, newnumber):
        self.number = newnumber

def get(pbook, name):
    """Loop through the phonebook in order.
    Return Entry if found. Else None
    """
    for entry in pbook:
        for alias in entry.aliaslist:
            if name == alias:
                return entry
    

def if_in(fun):
    def new(*args):
        if get(args[0], args[1]):
            return fun(*args)
        else:
            return not_found % args[0]
    return new

not_found = "%s not in phonebook"
def add(pbook, name, number):
    pbook.append(Entry(name, number))

def alias(pbook, name, newname):
    if not get(pbook, name) == None:
        get(pbook, name).alias(newname)
    else:
        return not_found % name

def lookup(pbook, name):
    temp = get(pbook, name)
    if not temp == None:
        return "%s has phonenumber %s" %(name, temp.number)
    else:
        return not_found % name

def change(pbook, name, number):
    if get(pbook, name):
        get(pbook, name).number = number
    else:
        return not_found % name
        
def save(pbook, filename):
    
    filename = str(filename)
    f = open(filename, 'w')
    for entry in pbook:
        num = str(entry.number)
        f.write(num + ";")
        for alias in entry.aliaslist:
            a = str(alias)
            f.write(a + ";")
        f.write("\n")
    f.close()
    
def load(filename):
    """Assume perfect filetype"""
    f = open(str(filename), 'r')
    entries = f.readlines()
    pbook = []
    for entry in entries:
        values = entry.split(';')
        e = Entry(number=values[0], name=values[1])
        if len(values) > 2:
            for i in range(len(values) - 2):
                e.alias(values[i + 2])
        pbook.append(e)
    
    return pbook
    
def exe(pbook, tree):
    """execute a tree i.e a list of statements which is
    a list of keywords and identifiers
    """

    succ = True
    res = ""
    for statement in tree:
        if statement[0] == parser.Keyword("add"):
            add(pbook, statement[1], statement[2])
        elif statement[0] == parser.Keyword("alias"):
            res = alias(pbook, statement[1], statement[2])
        elif statement[0] == parser.Keyword("lookup"):
            res = lookup(pbook, statement[1])
        elif statement[0] == parser.Keyword("change"):
            res = change(pbook, statement[1], statement[2])
        elif statement[0] == parser.Keyword("save"):
            save(pbook, statement[1])
        elif statement[0] == parser.Keyword("load"):
            pbook = load(statement[1])
            print pbook
        elif statement[0] == parser.Keyword("quit"):
            sys.exit(0)
            

        if not res == '':
            print res
            res = ''

prompt = "phonebook :> "
def main():
    pbook = []
    if len(sys.argv) > 1:
        for line in open(sys.argv[1], 'r'):
           print prompt,
           print line
           succ, tree = parser.parse(parser.lexer(line))
           exe(pbook, tree)
    else:
        while True:
            try:
                a = raw_input(prompt)
            except:
                break
            succ, tree = parser.parse(parser.lexer(a))
            exe(pbook, tree)

if __name__ == '__main__':
    main()
