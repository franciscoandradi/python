from flask import Flask

app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    return "Seja bem vindo!"  # Complete com a mensagem de boas-vindas

# Rota de saudação
@app.route('/saudacao/<nome>')
def saudacao(francisco):
    return "Olá, <nome>!" # Complete para retornar "Olá, <nome>!"

# Rodar o servidor
if __name__ == '__main__':
    app.run(debug=True)
