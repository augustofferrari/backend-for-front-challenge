
import random

from coin.models import Coin, CoinReview
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

COMMENTS = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Etiam vel tristique neque. Phasellus ullamcorper nunc iaculis malesuada vulputate. \
    Ut nec tincidunt turpis. Proin sagittis maximus vehicula.",
    "Aenean faucibus, ex sed egestas congue, odio metus volutpat nibh, nec vestibulum \
    turpis purus eu neque. Suspendisse eu dolor vitae magna blandit porta non a nibh. \
    Cras a vestibulum est. Pellentesque varius, lorem cursus dictum aliquet, \
    neque magna eleifend nisl, eu ullamcorper purus erat quis diam. ",
    "Duis nulla enim, feugiat id justo a, gravida viverra nunc. Nullam feugiat sodales\
    tortor non ullamcorper. Vestibulum odio est, ornare non mauris eu,",
    "Suspendisse iaculis est justo. Quisque dictum eget nisi quis pellentesque. Etiam auctor, \
    elit vel auctor eleifend, arcu felis aliquam tellus, a convallis ligula sem et est",
    "Suspendisse tempus, leo id aliquam fringilla, magna augue hendrerit nibh, sit amet condimentum \
    ex turpis eget nisi. Phasellus malesuada efficitur eros eget tincidunt. Nunc non aliquet nisi. ",
    "Nam pharetra semper mauris a sagittis. Integer in erat lacinia, sagittis neque eget, tempor justo.\
     Nulla mattis auctor mollis. Aenean orci orci, condimentum eu risus vitae, elementum finibus ",
    "Duis bibendum neque in sem mollis, non porttitor veli",
    "Quisque suscipit diam hendrerit augue convallis auctor.",
    "In sem mollis, non porttitor velit pulvinar. Quisque interdum ",
    "Mauris gravida efficitur erat, eget malesuada augue lacinia at",

]


class Command(BaseCommand):
    help = 'Create fake coin reviews'

    def get_random_comment(self):
        return random.choice(COMMENTS)

    def handle(self, *args, **options):
        try:
            coins = Coin.objects.all()
            users = list(User.objects.all().exclude(username="admin"))
            for coin in coins:
                # shuffle users
                users_list = users.copy()
                random.shuffle(users_list)
                for i in range(random.randint(0, len(users_list)-2)):
                    fake_review_data = {
                        "user": users_list[i],
                        "coin": coin,
                        "ranking": random.randint(1, 5),
                        "text": self.get_random_comment()
                    }
                    CoinReview.objects.get_or_create(**fake_review_data)
                pass
        except Exception as e:
            print(str(e))
            raise e
