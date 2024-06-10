import ply.yacc as yacc

# Importar tokens desde el lexer
from lexer import tokens

# Precedencia de operadores
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQEQ', 'EQEQEQ'),
    ('left', 'GT', 'LT', 'GTE', 'LTE'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('right', 'NOT'),
)

# Definición de la gramática
def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : var_declaration
                 | print_statement
                 | if_statement
                 | expression_statement'''
    p[0] = p[1]

def p_var_declaration(p):
    '''var_declaration : VARIABLESITA ID ASIGNACION expression SEMICOLON
                       | ENTERITO ID ASIGNACION expression SEMICOLON
                       | FLOTANTITO ID ASIGNACION expression SEMICOLON
                       | CARACTERCITO ID ASIGNACION expression SEMICOLON
                       | LOGIQUITO ID ASIGNACION expression SEMICOLON'''
    p[0] = ('var_declaration', p[1], p[2], p[4])

def p_print_statement(p):
    '''print_statement : IMPRIMIR LPAREN expression RPAREN SEMICOLON'''
    p[0] = ('print_statement', p[3])

def p_if_statement(p):
    '''if_statement : SHI LPAREN expression RPAREN LBRACE statement_list RBRACE else_statement'''
    p[0] = ('if_statement', p[3], p[6], p[8])

def p_else_statement(p):
    '''else_statement : SHINO LBRACE statement_list RBRACE
                      | empty'''
    if len(p) == 5:
        p[0] = p[3]
    else:
        p[0] = None

def p_expression_statement(p):
    '''expression_statement : expression SEMICOLON'''
    p[0] = ('expression_statement', p[1])

def p_expression(p):
    '''expression : expression SUMA expression
                  | expression RESTA expression
                  | expression MULTIPLICACION expression
                  | expression DIVISION expression
                  | expression EQEQ expression
                  | expression EQEQEQ expression
                  | expression GT expression
                  | expression LT expression
                  | expression GTE expression
                  | expression LTE expression
                  | expression AND expression
                  | expression OR expression
                  | NOT expression'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = (p[1], p[2])

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_literal(p):
    '''expression : NUMERO
                  | CADENA
                  | BOOLEANO
                  | ID'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Construcción del parser
parser = yacc.yacc()

