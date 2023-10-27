from ply import yacc
from echoLex import *

# import logging
# logging.basicConfig(
#     level=logging.INFO,
#     filename="parselog.txt"
# )


def p_statement(p):
    """statement : echo options string"""
    print("valid input")
    pass


def p_echo(p):
    """echo : ECHO"""
    pass


def p_string(p):
    """string : STRING"""
    pass


def p_options(p):
    """options : option options
    | empty"""
    pass


def p_empty(p):
    """empty :"""
    pass


def p_option(p):
    """option : OPTION"""


def p_error(p):
    print("invalid syntax")


parser = yacc.yacc()
x = input("enter : ")
parser.parse(x)
