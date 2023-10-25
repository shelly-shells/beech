from ply import lex

tokens = ("LS", "OPTION", "DIRECTORY")

def t_LS(t):
    r'ls'
    return t

def t_OPTION(t):
    r'-[alhRtsrudi]+|--help|--version|--all|--si'
    return t

def t_DIRECTORY(t):
    r'(\/([a-zA-Z0-9])+)+'
    return t

t_ignore ='   \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
    
lexer = lex.lex()
# lexer.input('ls /home/sus/hwow')
# while True:
#     tok = lexer.token()
#     if not tok:
#         break  # No more input
#     print(tok)