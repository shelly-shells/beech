from ply import lex

tokens = ("ECHO", "STRING", "OPTION")

# t_ECHO = r'echo'
# t_OPTION = r'-[en]|\*|\$'

precedence = (("left", "ECHO"), ("left", "OPTION"), ("left", "STRING"))


def t_ECHO(t):
    r"echo"
    return t


def t_OPTION(t):
    r"-[en]|\*|\$"
    return t


def t_STRING(t):
    r"\"[^\"]*\"|[^\n]+"
    return t


t_ignore = "    \t"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()
lexer.input("echo hi > file.txt")
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
