import ply.lex as lex 

tokens = ('IF', 'THEN','ELIF','ELSE','ENDIF','COMPARISON','VARIABLE','NUMBER','STRING','COMMAND')

t_ignore = ' \t\n'
def t_IF(t):
    r'if'
    return t

def t_THEN(t):
    r'then'
    return t

def t_ELIF(t):
    r'elif'
    return t 

def t_ELSE(t):
    r'else'
    return t

def t_ENDIF(t):
    r'fi'
    return t

def t_COMPARISON(t):
    r'=|>|<|!'
    return t

def t_COMMAND(t):
    r'statement'
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\'[^\']*\''
    t.value = t.value[1:-1]
    return t

def t_error(t):
    print("Illegal character: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# x= "if a>5 then statement elif a<=5 statement else statement fi"
# lexer.input(x)
# while True:
#     tok = lexer.token()
#     if not tok:
#         break  # No more input
#     print(tok)