from django.contrib import admin

from .models import Coin, CoinReview

# Register your models here.
admin.site.register(Coin)
admin.site.register(CoinReview)
