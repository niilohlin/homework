
class Token:
    """A token is either a Keyword or an Identifier
    """
    def __init__(self):
        self.token = ""
    @staticmethod
    def is_keyword(string):
        if string in "add lookup alias change save load quit alias_with_pn change_with_pn".split(' '):
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
    """Return a list of the string divided by the spaces.
    Remove ambiguity for the parser by changeing the change
    with phone number tokens to one
    """
    tokens = []
    words = string.split(' ')
    for i in range(len(words)):
        word = words[i]
        if Token.is_keyword(word):
            tokens.append(Keyword(word))
        else:
            tokens.append(Identifier(word))
            if i > 3 and (words[i - 3] == 'change' or words[i - 3] == 'alias'):
                tokens[i - 3] = Keyword(word + '_with_pn')
            
    return tokens
    
def expected_arguments(keyword):
    """Return the expected arguments for a given keyword"""
    if keyword in [Keyword("change_with_pn"), Keyword("alias_with_pn")]:
        return 3
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
    """Check if a statement has all proper arguments"""
    if len(statement) - 1 == expected_arguments(statement[0]):
        return True
    return False
    

def grammar(tree):
    """Check if a list of statements i.e a tree has the proper 
    number of arguments
    """
    for statement in tree:
        if not proper_arguments(statement):
            statementstring = " ".join(map(str,statement))
            return (False, """error, wrong number of arguments at\n \
%s. Expected %d. got %d""" % (statementstring, \
                        expected_arguments(statement[0]), \
                        len(statement) - 1))
    return (True, "")
                
        
    
def parse(tokens):
    """Return a tree of the given token list. Makeing a list of
    lists
    """
    tree = []
    for token in tokens:
        if isinstance(token, Keyword):
            tree.append([token])
        elif isinstance(token, Identifier):
            if len(tree) > 0:
                tree[len(tree) - 1].append(token)
            elif not token.token == "":
                return False, "%s is not a keyword" % token
    succ, msg = grammar(tree)
    if succ:
        return succ, tree    
    else:
        return succ, msg

