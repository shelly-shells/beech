import ply.lex as lex
tokens = ('FOR', 'VAR', 'IN', 'DO', 'DONE',
          'VALUE', 'COMMAND')

#precedence = (('left',  'FOR'),('left',  'IN'),('left',  'VALUE'),('left',  'DO'),('left',  'DONE'),('left',  'VAR'),('left',  'COMMAND'))

# '''t_FOR = r'for'
# t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'
# t_IN = r'in'
# t_DO = r'do'
# t_ignore = ' \t\n'
# '''

t_ignore = ' \t\n'
def t_FOR(t):
    r'for'
    return t

def t_IN(t):
    r'in'
    return t

def t_DONE(t):
    r'done'
    return t 

def t_DO(t):
    r'do'
    return t

def t_COMMAND(t):
    r'statement'
    return t

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_VALUE(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal character: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

x= "for i in 1 2 3 do i=i+1 done"
lexer.input(x)
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)