from ply import lex

tokens = ("echo", "options", "string", "empty")

t_echo = r'\\echo'
t_options = r'\\(-[en]) | \* | \$'


def t_string(t):
    r'\"[^\"]*\" | [^\t\n]+'     
    if t.value[0] == '"':
        t.value = t.value[1:-1]
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
