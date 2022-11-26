from rply import LexerGenerator


class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
      
        self.lexer.add("TEXT", '(""".*?""")|(".*?")|(\'.*?\')')
        self.lexer.add("DECIMAL", r"\d+\.\d+")
        self.lexer.add("INTEGER", r"\d+")
        self.lexer.add("OUTPUT", r"output(?!\w)|print(?!\w)|say(?!\w)")
        self.lexer.add("CONDITION", r"(?i)true(?!\w)|false(?!\w)") 
        self.lexer.ignore(r"//.*")  
        self.lexer.add("ADD", r"\+")
        self.lexer.add("SUB", r"-")
        self.lexer.add("MUL", r"\*")
        self.lexer.add("DIV", r"/")
        self.lexer.add("POW", r"\^")
        self.lexer.add("MOD", r"mod(?!\w)")
        self.lexer.add("=", r"=")
        self.lexer.add("NOT=", r"not=")
        self.lexer.add("<=", r"<=")
        self.lexer.add("<", r"<")
        self.lexer.add(">=", r">=")
        self.lexer.add(">", r">")
        self.lexer.add("AND", r"and")
        self.lexer.add("OR", r"or")
        self.lexer.add("NOT", r"not")
        self.lexer.add("REPEATUNTIL", r"repeat until(?!\w)")
        self.lexer.add("REPEAT", r"repeat(?!\w)")
        self.lexer.add("IF", r"if(?!\w)")
        self.lexer.add("ELSEIF", r"(else if)(?!\w)|(but if)(?!\w)|(otherwise if)(?!\w)")
        self.lexer.add("ELSE", r"else(?!\w)|otherwise(?!\w)")
        self.lexer.add("VARIABLE", "[a-zA-Z_][a-zA-Z0-9_]*")
        self.lexer.add("LPAREN", r"\(")
        self.lexer.add("RPAREN", r"\)")
        self.lexer.add("INDENT", r"\t")
        self.lexer.add("NEWLINE", r"\n")
        self.lexer.ignore(r"[ \r\f\v]+")

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()