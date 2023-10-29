from ply import lex

tokens = ("LS", "OPTION", "DIRECTORY", "OPTION_LONG")


def t_LS(t):
    r"ls"
    return t


def t_OPTION(t):
    r"-[acdghilporstuFDRS]+"
    return t


def t_OPTION_LONG(t):
    r"--help|--version|--all|--si"
    return t


def t_DIRECTORY(t):
    r"(\/([a-zA-Z0-9])+)+"
    return t


t_ignore = "   \t"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    t.lexer.skip(1)


lexer = lex.lex()

