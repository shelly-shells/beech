import ply.yacc as yacc 
from forLex import tokens

def p_for_loop(p):
    '''
        for_loop : FOR VAR IN values DO commands DONE 
        
    '''
    print("valid input")

def p_values(p):
    '''
        values : values value
               | value 
    '''

def p_value(p):
    '''
        value : VALUE
    '''

def p_commands(p):
    '''
        commands : command 
                 | commands command
    '''

def p_command(p):
    '''
        command : COMMAND
    '''

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()
data = input("Enter something: ")
result = parser.parse(data)


