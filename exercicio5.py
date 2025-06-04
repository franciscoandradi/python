from flask import Flask

app = Flask(__name__)

@app.route('/fecaf')
def fecaf():
    return 'Bem vindo(a)! A Universidade UniFecaf!'

app.run()
