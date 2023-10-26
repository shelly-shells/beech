import ply.yacc as yacc
from ifLex import tokens

def p_program(p):
    '''
    program : statement 
    '''

def p_statement(p):
    '''
    statement : if_statement | other_statement
    '''

def p_if_statement(p):
    '''
    if_statement : IF condition THEN statement ENDIF
                 | IF condition THEN statement elif_statments else_statement ENDIF
    '''

def p_elif_statements(p):
    '''
    elif_statements : elif_statement elif_statements 
                    | empty
    '''

def p_elif_statement(p):
    '''
    elif_statement : ELIF condition THEN statement
    '''

def p_else_statement(p):
    '''
    else_statement : ELSE statement
                   | empty
    '''

def p_condition(p):
    '''
    condition : expression COMPARISON expression
    '''

def p_expression(p):
    '''
    expression : variable | constant
    '''

def p_variable(p):
    '''
    variable : VARIABLE
    '''

def p_constant(p):
    '''
    constant : NUMBER | STRING 
    '''

def p_other_statement(p):
    '''
    other_statement : COMMAND 
    '''

def p_empty(p):
    '''
    empty : 
    '''
    pass

def p_error(p):
    print("Syntax error in input!")

data = input("Enter something: ")

parser = yacc.yacc()
result = parser.parse(data)

print(result)