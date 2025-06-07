from flask import Flask, render_template, request
import pymysql.cursors
import webbrowser
import threading
import os
import sys

if getattr(sys, 'frozen', False):
    # Se estiver rodando no .exe criado pelo PyInstaller
    base_path = sys._MEIPASS
else:
    # Rodando no script normal
    base_path = os.path.abspath(".")

template_dir = os.path.join(base_path, "templates")
app = Flask(__name__, template_folder=template_dir)

# Função para conectar ao banco de dados
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='meu_app_user',
        password='filmes@123',  # Altere se necessário
        database='movies',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

# Rota principal com ordenação
@app.route('/')
def index():
    sort = request.args.get('sort', 'movie_id')  # Ordenação padrão
    valid_sorts = ['movie_id', 'name', 'year']

    # Segurança: evitar SQL injection
    if sort not in valid_sorts:
        sort = 'movie_id'

    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM `movies_data` ORDER BY {sort}")
        movies = cursor.fetchall()
    connection.close()

    return render_template('index.html', movies=movies)

# Função para abrir o navegador automaticamente
def open_browser():
    webbrowser.open_new('http://127.0.0.1:3010/')

# Inicialização do app
if __name__ == '__main__':
    # Garante que o navegador só abrirá no processo principal do Flask
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        threading.Timer(1.5, open_browser).start()

    app.run(debug=True, port=3010)
