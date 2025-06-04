from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Lista global pra armazenar os itens (em memória)
itens = []

# Template HTML simples com form e lista
template = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <title>Adicionar Itens</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    input[type="text"] { padding: 8px; font-size: 16px; width: 250px; }
    button { padding: 8px 12px; font-size: 16px; margin-left: 8px; cursor: pointer; }
    ul { margin-top: 20px; list-style-type: disc; }
  </style>
</head>
<body>
  <h1>Adicionar Itens</h1>

  <form method="POST" action="{{ url_for('adicionar') }}">
    <input name="item" type="text" placeholder="Digite o item..." autocomplete="off" />
    <button type="submit">Adicionar</button>
  </form>

  <ul>
    {% for item in itens %}
      <li>{{ item }}</li>
    {% endfor %}
  </ul>
</body>
</html>
'''

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        item = request.form.get('item', '').strip()
        if item:
            itens.append(item)
        return redirect(url_for('adicionar'))

    return render_template_string(template, itens=itens)

if __name__ == '__main__':
    app.run()
