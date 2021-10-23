from django.contrib.auth.models import User
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create user for frontend'

    def handle(self, *args, **options):
        user = User.objects.create(
            username="front_user",
            first_name="Front",
            last_name="User",
            email="front_user@a.com",
        )
        user.set_password("test_password")
        user.save()
