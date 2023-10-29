from ply import lex

tokens = ("CHMOD", "OPTION", "FILE")


def t_CHMOD(t):
    r"chmod"
    return t


def t_OPTION(t):
    r"([1-7]{3})|(([aA]|[uUgGoO]{1,3})?[\+\-][rwxRWX]{1,3})"
    return t


def t_FILE(t):
    r"([a-zA-Z0-9]+)\.([a-zA-Z0-9]+)"
    return t


t_ignore = "  \t"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    t.lexer.skip(1)


lexer = lex.lex()

