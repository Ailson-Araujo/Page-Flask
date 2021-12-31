from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/basedados')
def base_dados():
    name_title = 'Base de Dados'
    return render_template('basedados.html', name_title = name_title)

@app.route('/mensagem')
def message():
    name_title = 'Mensagem'
    return render_template('mensagem.html', name_title = name_title)

@app.route('/plotagem')
def plotagem():
    name_title = 'Plotagem'
    return render_template('plotagem.html', name_title = name_title)

@app.route('/return')
def return_page():
    return render_template('return.html')

@app.route('/visualizacao')
def visualizacao():
    name_title = 'Visualização de Dados'
    return render_template('visualizacao.html', name_title = name_title)