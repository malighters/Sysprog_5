import ply.lex as lex

tokens = (
    'NUMBER',        # num
    'PLUS',          # +
    'MINUS',         # -
    'MULTIPLY',      # *
    'DIVIDE',        # /
    'LPARENTHESIS',  # (
    'RPARENTHESIS',  # )
    'POWER',         # ^
    'IDENTIFIER',    # names for variables
    'EQUALS',        # =
)

# Regex patterns
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPARENTHESIS = r'\('
t_RPARENTHESIS = r'\)'
t_POWER = r'\^'
t_EQUALS = r'='


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)  # Change to float
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print('Некоректний символ ' + t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
