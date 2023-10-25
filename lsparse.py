from ply import yacc
from lslex import *

def p_statement(p):
    '''statement : ls option directory'''
    pass

def p_ls(p):
    '''ls : LS'''
    pass

def p_option(p):
    '''option : option options
                | empty'''
    pass

def p_directory(p):
    '''directory : directories directory
                   | empty'''
    pass

def p_empty(p):
    '''empty :'''
    pass

def p_options(p):
    '''options : OPTION'''
    pass

def p_directories(p):
    '''directories : DIRECTORY'''
    pass

def p_error(p):
    print("Invalid syntax")
    
    
parser = yacc.yacc()
x = input("enter : ")
# lexer.input(x)
parser.parse(x)