
class Token:
    def __init__(self):
        self.token = ""
    
    def __eq__(self, other):
        return self.token == other.token
        
    def __repr__(self):
        return self.token
    def __str__(self):
        return self.token
    
class Identifier(Token):
    def __init__(self, string):
        self.token = string
    
    def __repr__(self):
        return "Identifier(%s)" % self.token

class Keyword(Token):
    def __init__(self, string):
        self.token = string
        self.arg_type = []
    
    def __repr__(self):
        return "Keyword(%s)" % self.token

class Add(Keyword):
    def __init__(self):
        Keyword(self, "add")
        self.arg_type = [Identifier, Identifier]

class Alias(KeyWord):
    def __init__(self):
        Keyword(self, "alias")
        self.arg_type = [Identifier]
        

class Change(KeyWord):
    def __init__(self):
        Keyword(self, "change")
        self.arg_type = [Identifier, Identifier]
        
class Save(KeyWord):
    def __init__(self):
        Keyword(self, "save")
        self.arg_type = [Identifier]


class Load(KeyWord):
    def __init__(self):
        Keyword(self, "load")
        self.arg_type = [Identifier]

class Quit(KeyWord):
    def __init__(self):
        Keyword(self, "quit")
        self.arg_type = []

def lexer(string):
    tokens = []
    for word in string.split(' '):
        if Token.is_keyword(word):
            tokens.append(Keyword(word))
        else:
            tokens.append(Identifier(word))
    return tokens
    
def expected_arguments(keyword):
    if keyword in [Keyword("add"), Keyword("alias"), 
            Keyword("change")]:
        return 2
    elif keyword in [Keyword('lookup'), Keyword('save'), 
            Keyword('load')]:
        return 1
    elif keyword == Keyword('quit'):
        return 0
    else:
        return -1

def proper_arguments(statement):
    if len(statement) - 1 == expected_arguments(statement[0]):
        return True
    return False
    

def grammar(tree):
    for statement in tree:
        if not proper_arguments(statement):
            statementstring = " ".join(map(str,statement))
            return (False, """error, wrong number of arguments at\n \
%s. Expected %d""" % (statementstring, \
                        expected_arguments(statement[0])))
    return (True, "")
                
        
    
def parse(tokens):
    tree = []
    for token in tokens:
        if isinstance(token, Keyword):
            tree.append([token])
        elif isinstance(token, Identifier):
            tree[len(tree) - 1].append(token)
    succ, msg = grammar(tree)
    if not succ:
        print msg
        return succ, tree
    else:
        return succ, tree    

