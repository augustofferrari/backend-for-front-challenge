import datetime
import random

import requests
from coin.models import Coin
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

COIN_URL = "https://api.coingecko.com/api/v3"


class Command(BaseCommand):
    help = 'Load fake coins'

    def random_date(self):
        """
        Random date
        """
        start = datetime.datetime.strptime(
            "2021-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
        end = datetime.datetime.strptime(
            "2021-10-10 00:00:00", "%Y-%m-%d %H:%M:%S")
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        return start + datetime.timedelta(seconds=random_second)

    def create_coin(self, coin):
        coin_data = {
            "name": coin.get("name"),
            "abbreviation": coin.get("symbol"),
            "current_price": random.random()*1000,
            "low_price": random.random()*1000,
            "high_price": random.random()*1000,
            "volume": random.randint(100, 500000),
            "created_at": self.random_date(),
        }
        Coin.objects.get_or_create(**coin_data)
        pass

    def get_coin_list(self):
        url = f"{COIN_URL}/coins/list"
        response = requests.get(url)
        print(response.json()[:15])
        return response.json()[:15]

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                coins = self.get_coin_list()
                for coin in coins:
                    self.create_coin(coin)
        except Exception as e:
            print(str(e))
            raise e
