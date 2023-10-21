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
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)


import ply.yacc as yacc 

def p_for_loop(p):
    '''
        for_loop : FOR VAR IN values DO commands DONE 
    '''

def p_values(p):
    '''
        values : values value 
    '''

def p_value(p):
    '''
        value : VALUE
    '''

def p_commands(p):
    '''
        commands : command 
                 | commands command 
                 | for_loop 
    '''

def p_command(p):
    '''
        command : COMMAND
    '''

def p_error(p):
    print("Syntax error in output!")

parser = yacc.yacc()

data = input("Enter something: ")
result = parser.parse(data)

print(result)

