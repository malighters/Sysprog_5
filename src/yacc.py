import ply.yacc as yacc
from src.lex import tokens


# Priority of operations
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('nonassoc', 'UMINUS'),
    ('left', 'POWER'),
)

var = {}


def p_statement(p):
    '''
        statement : assignment
                  | expression
    '''
    p[0] = p[1]


def p_assignment(p):
    'assignment : IDENTIFIER EQUALS expression'
    var[p[1]] = p[3]
    p[0] = p[3]


def p_expression_operations(p):
    '''expression : expression PLUS expression
                      | expression MINUS expression
                      | expression MULTIPLY expression
                      | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_uminus(p):
    "expression : MINUS expression %prec UMINUS"
    p[0] = -p[2]


def p_expression_parenthesis(p):
    "expression : LPARENTHESIS expression RPARENTHESIS"
    p[0] = p[2]


def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]


def p_expression_power(p):
    'expression : expression POWER expression'
    p[0] = p[1] ** p[3]


def p_error(p):
    print('Знайдено синтаксичну помилку.')


def p_expression_variable(p):
    'expression : IDENTIFIER'
    try:
        p[0] = var[p[1]]
    except LookupError:
        print('Не знайдено змінну: ' + p[1])
        p[0] = 0


parser = yacc.yacc()
