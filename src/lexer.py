import ply.lex as lex

# Palabras reservadas
reserved = {
    'variablesita': 'VARIABLESITA',
    'enterito': 'ENTERITO',
    'flotantito': 'FLOTANTITO',
    'caractercito': 'CARACTERCITO',
    'logiquito': 'LOGIQUITO',
    'shi': 'SHI',
    'shino': 'SHINO',
    'muestrica': 'IMPRIMIR'
}

# Lista de tokens
tokens = [
    'ID', 'NUMERO', 'CADENA', 'BOOLEANO', 'ASIGNACION', 'SEMICOLON',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION', 'EQEQ', 'EQEQEQ', 
    'GT', 'LT', 'GTE', 'LTE', 'AND', 'OR', 'NOT'
] + list(reserved.values())

# Expresiones regulares para tokens simples
t_ASIGNACION = r'='
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_EQEQ = r'=='
t_EQEQEQ = r'==='
t_GT = r'>'
t_LT = r'<'
t_GTE = r'>='
t_LTE = r'<='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

# Definiciones de tokens complejos
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = str(t.value[1:-1])  # Eliminar las comillas
    return t

def t_BOOLEANO(t):
    r'true|false'
    t.value = t.value == 'true'
    return t

# Ignorar espacios, tabulaciones y nuevas líneas
t_ignore = ' \t\n'

# Manejo de errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()
