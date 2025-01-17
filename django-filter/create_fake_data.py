import os
from random import choice, sample, random

import django
from django.contrib.auth import get_user_model
from faker import Faker
from faker.providers import isbn, date_time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trying_out_django_filter.settings')
django.setup()

from main.models import *

fake = Faker()
fake.add_provider(isbn)
fake.add_provider(date_time)


for _ in range(0):
    Genre(
        name=fake.word().capitalize(),
    ).save()


for _ in range(1000):
    Author(
        name=fake.name(),
        date_of_birth=fake.date_object(),
    ).save()


for _ in range(0):
    b = Book(
        title=fake.sentence(nb_words=6)[:-1],
        isbn=fake.isbn13(separator=''),
        summary=fake.text(max_nb_chars=200),
        price=random() * 100,
        publication_date=fake.date_object(),
        author=choice(Author.objects.all()),
    )
    b.save()
    b.genres.add(
        *sample(
            list(Genre.objects.all()),
            k=2,
        ),
    )
