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
    
    def __repr__(self):
        return str(self.aliaslist) + " " + str(self.number)



def remove(pbook, name, number):
    """Return a new phonebook with entry containing name
    and number removed
    """
    if get(pbook, name, number):
        return filter(lambda entry: (entry.number != number) or \
                (not name in entry.aliaslist), pbook), ""
    else:
        return pbook, "%s with number %s not in phonebook" % (name, number)
        

def get_all(pbook, name):
    """Return every entry that has name
    """
    res = []
    for entry in pbook:
        for alias in entry.aliaslist:
            if name == alias:
                res.append(entry)
    return res
        
def get(pbook, name, number=None):
    """Loop through the phonebook in order.
    Return Entry if found. Else None
    """
    
    for entry in pbook:
        if not number:
            for alias in entry.aliaslist:
                if name == alias:
                    return entry
        else:
            if number == entry.number:
                for alias in entry.aliaslist:
                    if name == alias:
                        return entry
                    
    
not_found = "%s not in phonebook"
def add(pbook, name, number):
    """Return a new phonebook with name and number added"""
    res = pbook[:]
    if not get(pbook, name):
        res.append(Entry(name, number))
        return res, ""
    else:
        return res, "%s already in phonebook" % name
    

def alias(pbook, name, newname):
    """Return a new phonebook with newname aliased to name
    if name is in phonebook, else return an error string
    """
    res = pbook[:]
    if get(pbook, name):
        
        get(res, name).alias(newname)
        return res, ""
    else:
        return res, not_found % name

def lookup(pbook, name):
    """Return a string that describes the presence of name
    in pbook
    """
    temp = get_all(pbook, name)
    if temp:
        return reduce((lambda x,y:x+y), 
                map(lambda num:
                    str(name) + " has phonenumber %s\n" %
                    num.number, temp)).strip('\n')
#        return "%s has phonenumber %s" %(name, temp.number)
    else:
        return not_found % name

def change(pbook, name, number):
    res = pbook[:]
    if get(res, name):
        get(res, name).number = number
        return res, ""
    else:
        return res, not_found % name
    
def change_with_pn(pbook, name, number, newnumber):
    temp = get(pbook, name, number)
    res = pbook[:]
    if temp:
        get(res, name, number).number = newnumber
        return res, ""
    else:
        return res, not_found + "with number %s" % (name, number)
        
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
    """Load a database by generating code for the interpreter 
    to execute. Return a new phonebook
    """
    try:
        f = open(str(filename), 'r')
    except:
        print "oops, file not found"
        return []
    entries = f.readlines()
    pbook = []
    for entry in entries:
        values = entry.split(';')
        lexed = parser.lexer("add %s %s" % (values[1], values[0]))
        succ, parsed = parser.parse(lexed)
        if succ:
            pbook = exe(pbook, parsed)
        else:
            print "error, bad filetype"
            return []
        if len(values) > 2:
            for i in range(len(values) - 2):
                lexed = parser.lexer("alias %s %s" % (values[1], \
                    values[i + 2]))
                succ, parsed = parser.parse(lexed)
                if succ:
                    pbook = exe(pbook, parsed)
                else:
                    print "error, bad filetype"
                    return []
    f.close()
    return pbook
    
def exe(pbook, tree):
    """execute a tree i.e a list of statements which is
    a list of keywords and identifiers
    """

    succ = True
    res = ""
    for statement in tree:
        if statement[0] == parser.Keyword("add"):
            pbook, res  = add(pbook, statement[1], statement[2])
        elif statement[0] == parser.Keyword("alias"):
            pbook, res = alias(pbook, statement[1], statement[2])
        elif statement[0] == parser.Keyword("lookup"):
            res = lookup(pbook, statement[1])
        elif statement[0] == parser.Keyword("change"):
            pbook, res = change(pbook, statement[1], statement[2])
        elif statement[0] == parser.Keyword("save"):
            save(pbook, statement[1])
        elif statement[0] == parser.Keyword("load"):
            pbook = load(statement[1])
        elif statement[0] == parser.Keyword("quit"):
            sys.exit(0)
        elif statement[0] == parser.Keyword("remove"):
            pbook, res = remove(pbook, statement[1], statement[2])
        elif statement[0] == parser.Keyword("change_with_pn"):
            pbook, res = change_with_pn(pbook, statement[1], statement[2], statement[3])
            

        if not res == '':
            print res
            res = ''
    return pbook

prompt = "phonebook :> "
def main():
    pbook = []
    if len(sys.argv) > 1:
        # if a file is an argument
        for line in open(sys.argv[1], 'r'):
            l = line.strip('\n')
            print prompt,
            print l
            succ, tree = parser.parse(parser.lexer(l))
            if succ:
                pbook = exe(pbook, tree)
            else:
                print tree
    else:
        while True:
            try:
                a = raw_input(prompt)
            except:
                break
            succ, tree = parser.parse(parser.lexer(a))
            if len(tree) == 0:
                print "not a keyword"
            elif succ:
                pbook = exe(pbook, tree)
            elif not succ:
                print tree

if __name__ == '__main__':
    #go if not an imported module
    main()
