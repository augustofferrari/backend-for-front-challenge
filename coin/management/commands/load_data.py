from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create fake coin reviews'

    def handle(self, *args, **options):

        call_command("load_coins")
        call_command("load_users")
        call_command("load_reviews")
        call_command("load_front_user")
