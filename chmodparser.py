from ply import yacc
from chmodlex import *

def p_statement(p):
    '''statement : chmod option file'''
    pass

def p_chmod(p):
    '''chmod : CHMOD'''
    pass

def p_option(p):
    '''option : OPTION'''
    pass

def p_file(p):
    '''file : FILE'''
    pass


def p_error(p):
    print("Invalid syntax")
    
parser = yacc.yacc()
x = input("enter : ")
parser.parse(x)