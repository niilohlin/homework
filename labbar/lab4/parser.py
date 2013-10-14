
class Token:
    def __init__(self):
        self.token = ""
    @staticmethod
    def is_keyword(string):
        if string in "add lookup alias change save load quit".split(' '):
            return True
        return False
    
    
    @staticmethod
    def is_identifier(string):
        return not Token.is_keyword(string)
    
    def __eq__(self, other):
        return self.token == other.token
        
    def __repr__(self):
        return self.token
    def __str__(self):
        return self.token
    
class Keyword(Token):
    def __init__(self, string):
        if Keyword.is_keyword(string):
            self.token = string
        else:
            raise "error, not a keyword"
    
    def __repr__(self):
        return "Keyword(%s)" % self.token

class Identifier(Token):
    def __init__(self, string):
        if Identifier.is_identifier(string):
            self.token = string
        else:
            raise "error, not a identifier"
            
    def __repr__(self):
        return "Identifier(%s)" % self.token



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

