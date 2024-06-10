class Interpreter:
    def __init__(self):
        self.variables = {}

    def eval(self, node):
        if isinstance(node, tuple):
            if node[0] == 'program':
                return self.eval_program(node)
            elif node[0] == 'var_declaration':
                return self.eval_var_declaration(node)
            elif node[0] == 'print_statement':
                return self.eval_print_statement(node)
            elif node[0] == 'if_statement':
                return self.eval_if_statement(node)
            elif node[0] == 'expression_statement':
                return self.eval_expression(node[1])
            elif node[0] == 'concat':
                return self.eval_concat(node)
            else:
                return self.eval_expression(node)
        else:
            return self.eval_literal(node)

    def eval_program(self, node):
        for statement in node[1]:
            result = self.eval(statement)
        return result

    def eval_var_declaration(self, node):
        var_type, var_name, expression = node[1], node[2], node[3]
        value = self.eval(expression)
        self.variables[var_name] = value

    def eval_print_statement(self, node):
        value = self.eval(node[1])
        print(value)
        return value

    def eval_if_statement(self, node):
        condition = self.eval(node[1])
        if condition:
            return self.eval_program(('program', node[2]))
        elif node[3]:
            return self.eval_program(('program', node[3]))
        return None

    def eval_concat(self, node):
        left = self.eval(node[1])
        right = self.eval(node[2])
        return str(left) + str(right)

    def eval_expression(self, node):
        if isinstance(node, tuple):
            operator = node[0]
            left = self.eval(node[1])
            right = self.eval(node[2])
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right
            elif operator == '/':
                return left / right
            elif operator == '==':
                return left == right
            elif operator == '===':
                return left is right
            elif operator == '>':
                return left > right
            elif operator == '<':
                return left < right
            elif operator == '>=':
                return left >= right
            elif operator == '<=':
                return left <= right
            elif operator == '&&':
                return left and right
            elif operator == '||':
                return left or right
            elif operator == '!':
                return not right
        elif isinstance(node, str):
            if node.startswith('"') and node.endswith('"'):
                return node[1:-1]  # Eliminar las comillas de la cadena
            if node in self.variables:
                return self.variables[node]
            return node
        return node

    def eval_literal(self, node):
        if isinstance(node, str):
            if node in self.variables:
                return self.variables[node]
            if node.startswith('"') and node.endswith('"'):
                return node[1:-1]  # Eliminar las comillas de la cadena
        return node

interpreter = Interpreter()