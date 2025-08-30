import csv
import random
import webbrowser
from flask import Flask, render_template, request, redirect, url_for, jsonify
from pathlib import Path
from threading import Timer


app = Flask(__name__)
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'data'

NOT_WATCHED_MOVIES = DATA_DIR / 'list_movies.csv'
WATCHED_MOVIES = DATA_DIR / 'watched.csv'


def load_movies(path: Path):
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def write_movies(path: Path, data):
    if not data:
        return
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


@app.route('/', methods=['GET'])
def index():
    query = request.args.get('q', '').lower()
    status = request.args.get('status', '')
    sort = request.args.get('sort', '')

    # Carrega as duas listas
    not_watched = load_movies(NOT_WATCHED_MOVIES)
    for movie in not_watched:
        movie['Watched'] = 'No'

    watched = load_movies(WATCHED_MOVIES)
    for movie in watched:
        movie['Watched'] = 'Yes'

    # Junta as listas
    movies = not_watched + watched

    # Filter by name
    if query:
        movies = [movie for movie in movies if query in movie['Name'].lower()]

    # Filter by status
    if status in ['Yes', 'No']:
        movies = [movie for movie in movies if movie['Watched'] == status]

    # Sort
    if sort == 'asc':
        movies.sort(key=lambda x: x['Name'].lower())
    elif sort == 'desc':
        movies.sort(key=lambda x: x['Name'].lower(), reverse=True)

    random_movie = random.choice(movies) if movies else None

    return render_template(
        'index.html',
        movies=movies,
        random_movie=random_movie,
        query=query,
        status=status,
        sort=sort)


@app.route('/mark_as_watched/<name>')
def mark_as_watched(name: str):
    # Load lists
    not_watched = load_movies(NOT_WATCHED_MOVIES)
    watched = load_movies(WATCHED_MOVIES)

    # Procura o filme na lista de não assistidos
    for i, movie in enumerate(not_watched):
        if movie['Name'].lower() == name.lower():
            watched.append(movie)
            del not_watched[i]
            break

    write_movies(NOT_WATCHED_MOVIES, not_watched)
    write_movies(WATCHED_MOVIES, watched)

    return redirect(url_for('index'))


@app.route('/toggle', methods=['POST'])
def toggle_watched():
    data = request.get_json()
    name = data.get('name')
    watched_status = data.get('watched') == 'Yes'

    not_watched = load_movies(NOT_WATCHED_MOVIES)
    watched = load_movies(WATCHED_MOVIES)

    if watched_status:
        # Move de não assistido para assistido
        for i, movie in enumerate(not_watched):
            if movie['Name'].lower() == name.lower():
                watched.append(movie)
                del not_watched[i]
                break
    else:
        # Move de assistido para não assistido
        for i, movie in enumerate(watched):
            if movie['Name'].lower() == name.lower():
                not_watched.append(movie)
                del watched[i]
                break

    write_movies(NOT_WATCHED_MOVIES, not_watched)
    write_movies(WATCHED_MOVIES, watched)

    return jsonify(success=True)


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5001")


if __name__ == "__main__":
    Timer(0.1, open_browser).start()
    app.run(debug=False, use_reloader=False, port=5001)
