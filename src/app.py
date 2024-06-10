from flask import Flask, request, render_template
from lexer import lexer
from my_parser import parser
from interpreter import interpreter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    code = request.form['code']
    lexer.input(code)
    
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(str(tok))
    
    try:
        result = parser.parse(code)
        if result:
            result_str = interpret(result)
        else:
            result_str = "Syntax error: invalid input"
    except Exception as e:
        result_str = f"Error: {str(e)}"
    
    return render_template('index.html', tokens=tokens, result=result_str)

def interpret(parse_tree):
    return interpreter.eval(parse_tree)

if __name__ == '__main__':
    app.run(debug=True)
