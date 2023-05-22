from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class MovieForm(FlaskForm):
    title = StringField("Название фильма", validators=[
        DataRequired(message='Поле "Название фильма" не может быть пустым'),
        Length(max=255, message="Название фильма не может быть более 255 символов")
    ])
    description = TextAreaField("Описание фильма", validators=[
        DataRequired(message='Поле "Описание фильма" не может быть пустым')
    ])
    image = FileField("Постер", validators=[
        DataRequired(message='Поле "Постер" не может быть пустым')
    ])
    submit = SubmitField("Добавить фильм")


class ReviewForm(FlaskForm):
    name = StringField("Имя", validators=[
        DataRequired(message='Поле "Имя" не может быть пустым'),
        Length(max=255, message="Имя не может быть более 255 символов")
    ])
    text = TextAreaField("Отзыв", validators=[
        DataRequired(message='Поле "Отзыв" не может быть пустым')
    ])
    rating = SelectField("Оценка", choices=list(range(1, 11)), default=10)
    submit = SubmitField("Добавить отзыв")
