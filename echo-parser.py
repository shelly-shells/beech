from echoLex import tokens
from ply import yacc

def p_statement(p):
    '''statement : ECHO option STRING'''
    pass

def p_option(p):
    ''' option : option options | empty'''
    if len(p) > 1:
        if not hasattr(p[-1], 'append'):
            p[-1] = [p[-1]]
        p[-1].append(p[1])
    else:
        p[0] = []
        
def p_empty(p):
    'empty: '
    pass

def p_error(p):
    print("invalid syntaax")
    
parser = yacc.yacc()

x = input()
parser.parse(x)

