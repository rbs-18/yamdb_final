from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date

from users.models import User

MIN_SCORE = 1
MAX_SCORE = 10


def validate_year(value):
    this_year = date.today().year
    if value > this_year:
        raise ValidationError('Нельзя указывать год из будущего')


class Genre(models.Model):
    """Модель для жанра."""
    name = models.CharField(
        max_length=256,
        unique=True,
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    """Модель для категории."""
    name = models.CharField(
        max_length=256,
        unique=True,
    )
    slug = models.SlugField(
        unique=True,
    )

    def __str__(self):
        return self.name


class Title(models.Model):
    """Модель для заголовка."""
    name = models.CharField(
        max_length=200,
    )
    year = models.PositiveSmallIntegerField(
        validators=[validate_year]
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
    )
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        through_fields=('title', 'genre'),
        related_name='titles',
    )
    description = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'category'],
                name='unique_name_category'
            )
        ]

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    """Модель для настройки консоли администратора."""
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.title} {self.genre}'


class Review(models.Model):
    """Модель для ревью."""
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    score = models.IntegerField(
        validators=(
            MinValueValidator(
                MIN_SCORE,
                message='Нельзя выбрать оценку меньше 1!',
            ),
            MaxValueValidator(
                MAX_SCORE,
                message='Нельзя выбрать оценку больше 10!',
            )
        ))
    pub_date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_title_author'
            )
        ]

    def __str__(self):
        return self.text[:25]


class Comment(models.Model):
    """Модель для комментария."""
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.text[:25]
