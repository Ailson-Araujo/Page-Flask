from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/basedados')
def base_dados():
    return render_template('basedados.html')

@app.route('/mensagem')
def message():
    return render_template('mensagem.html')

@app.route('/plotagem')
def plotagem():
    return render_template('plotagem.html')

@app.route('/return')
def return_page():
    return render_template('return.html')

@app.route('/visualizacao')
def visualizacao():
    return render_template('visualizacao.html')