from ply import yacc
from lslex import tokens


def p_statement(p):
    """statement : ls option directory"""
    print("Valid input")
    pass


def p_ls(p):
    """ls : LS"""
    pass


def p_option(p):
    """option : OPTION
    | OPTION_LONG"""
    pass


def p_directory(p):
    """directory : DIRECTORY
    | empty"""
    pass


def p_empty(p):
    """empty :"""
    pass


def p_error(p):
    print("Invalid syntax")


parser = yacc.yacc()
x = input("enter : ")
parser.parse(x)
