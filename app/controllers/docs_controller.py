from app import app, db_session
from flask import render_template, redirect
from ..data.games import Game
from requests import get


@app.route('/docs')
def docs():
    urls = {
        'Документы': 'documents',
        'Игры, методики диагностики ребенка': 'games_and_methodics',
        'Свечки': 'candle',
        'Шаблоны коллективного творческого дела': 'templates',
        'Примеры отрядного уголка': 'detachment_corner',
        'Правила составления план-сеток мероприятий': 'plans_of_events',
    }
    return render_template("docs.html", title="Документация и методички для вожатых", urls=urls, get=get)


@app.route('/docs/documents')
def documents():
    return render_template("docs/documents.html", title="Основные документы", get=get)


@app.route('/docs/games_and_methodics')
def games_and_methodics():
    db_sess = db_session.create_session()
    games = db_sess.query(Game).all()
    return render_template("docs/games_and_methodics.html", title="Игры и методики диагностики ребенка", games=games, get=get)


@app.route('/docs/candle')
def candle():
    return render_template("docs/candle.html", title="Свечки", get=get)


@app.route('/docs/templates')
def templates():
    return render_template("docs/templates.html", title="Шаблоны", get=get)


@app.route('/docs/detachment_corner')
def detachment_corner():
    return render_template("docs/detachment_corner.html", title="Отрядный уголок", get=get)


@app.route('/docs/plans_of_events')
def plans_of_events():
    return render_template("docs/plans_of_events.html", title="План-сетки мероприятий", get=get)