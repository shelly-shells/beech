import ply.lex as lex
tokens = ('FOR', 'VAR', 'IN', 'DO', 'DONE',
          'VALUE', 'COMMAND')

t_FOR = r'for'
t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_IN = r'in'
t_DO = r'do'

def t_VALUE(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMMAND(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*|[+\-*/=<>!&|]+'
    return t

def t_error(t):
    print("Illegal character: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()