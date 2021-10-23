
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

FAKE_USERS = [
    {
        "username": "manco001",
        "first_name": "Andres",
        "last_name": "Robertson",
        "email": "ar@a.com",
    },
    {
        "username": "genius_1",
        "first_name": "Juan",
        "last_name": "Perez",
        "email": "jp@a.com",
    },
    {
        "username": "robert_24",
        "first_name": "Roberto",
        "last_name": "Lamas",
        "email": "robert@a.com",
    },
    {
        "username": "pizzarower",
        "first_name": "Angel",
        "last_name": "luz",
        "email": "pizzarower@a.com",
    },
    {
        "username": "senaterye",
        "first_name": "Bautista",
        "last_name": "Lopez",
        "email": "robert@a.com",
    },
    {
        "username": "covetprincess",
        "first_name": "Teodoro",
        "last_name": "Tutember",
        "email": "robert@a.com",
    },
    {
        "username": "bluethe",
        "first_name": "Mireia",
        "last_name": "Paulino",
        "email": "bluethe@a.com",
    }
]


class Command(BaseCommand):
    help = 'Load fake users'

    def handle(self, *args, **options):
        try:
            for user in FAKE_USERS:
                User.objects.get_or_create(**user)
        except Exception as e:
            print(str(e))
            raise e
