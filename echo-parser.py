from ply import yacc

def p_echo(p):
    '''s : echo eVar nVar starVar dollarVar args'''
    pass

def p_minus_e(p):
    '''eVar : -e | empty'''
    pass

def p_minus_n(p):
    '''nVar : -n | empty'''
    
def p_star(p):
    '''starVar : * | empty'''
    pass

def p_dollar(p):
    '''dollarVar : $ | empty'''
    pass

def p_args(p):
    '''args : ID args'''
    pass

def p_args_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print("Syntax error")
    pass

parser = yacc.yacc()
s = input("enter something\n")
parser.parse(s)   
