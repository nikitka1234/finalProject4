from flask import render_template, redirect, url_for

from . import app, db
from .models import Review, Movie
# from .forms import


def index():
    movies = Movie.query.all()

    return render_template("index.html", movies=movies)


def movie(id):
    movie_object = Movie.query.get(id)

    if movie_object.review:
        avg_rating = round(sum([r.rating for r in movie_object.review]) / len(movie_object.review), 1)
    else:
        avg_rating = 0

    return render_template("movie.html", movie=movie_object, avg_rating=avg_rating)


def add_movie():
    return "Добавить фильм"


def reviews():
    return "Все отзывы"


def delete_review(id):
    return "Удалить отзыв"


app.add_url_rule("/", "index", index)
app.add_url_rule("/movie/<int:id>", "movie", movie)
app.add_url_rule("/add_movie", "add_movie", add_movie)
app.add_url_rule("/reviews", "reviews", reviews)
app.add_url_rule("/delete_review/<int:id>", "delete_review", delete_review)
