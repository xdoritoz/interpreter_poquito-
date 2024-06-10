import ply.yacc as yacc
from lexer import tokens

# Definición de la precedencia para operadores
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQEQ', 'EQEQEQ'),
    ('left', 'GT', 'LT', 'GTE', 'LTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'NOT'),
)

# Definición de reglas gramaticales
def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : assignment_statement
                 | expression_statement
                 | print_statement
                 | if_statement
                 | while_statement
                 | for_statement'''
    p[0] = p[1]

def p_assignment_statement(p):
    'assignment_statement : VARIABLESITA type ID ASIGNACION expression SEMICOLON'
    p[0] = ('assign', p[2], p[3], p[5])

def p_type(p):
    '''type : ENTERITO
            | FLOTANTITO
            | CARACTERCITO
            | LOGIQUITO'''
    p[0] = p[1]

def p_expression_statement(p):
    'expression_statement : expression SEMICOLON'
    p[0] = p[1]

def p_print_statement(p):
    'print_statement : IMPRIMIR LPAREN expression RPAREN SEMICOLON'
    p[0] = ('print', p[3])

def p_if_statement(p):
    'if_statement : IF LPAREN expression RPAREN LBRACE statement_list RBRACE else_statement'
    p[0] = ('if', p[3], p[6], p[8])

def p_else_statement(p):
    '''else_statement : ELSE LBRACE statement_list RBRACE
                      | empty'''
    if len(p) == 5:
        p[0] = ('else', p[3])
    else:
        p[0] = None

def p_while_statement(p):
    'while_statement : WHILE LPAREN expression RPAREN LBRACE statement_list RBRACE'
    p[0] = ('while', p[3], p[6])

def p_for_statement(p):
    'for_statement : FOR LPAREN assignment_statement expression_statement expression RPAREN LBRACE statement_list RBRACE'
    p[0] = ('for', p[3], p[4], p[5], p[8])

def p_expression(p):
    '''expression : ID
                  | ENTERO
                  | DECIMAL
                  | LOGICO
                  | CADENA
                  | expression PLUS expression
                  | expression PLUSPLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression AND expression
                  | expression OR expression
                  | expression EQEQ expression
                  | expression EQEQEQ expression
                  | expression GT expression
                  | expression GTE expression
                  | expression LT expression
                  | expression LTE expression
                  | NOT expression'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = (p[2], p[1], p[3])

def p_empty(p):
    'empty :'
    p[0] = None

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Construcción del parser
parser = yacc.yacc()
