from django.contrib.auth.models import User
from django.db import models
from django.db.models import constraints
from django.db.models.base import Model


# Create your models here.
class Coin(models.Model):
    name = models.CharField(unique=True, max_length=250)
    abbreviation = models.CharField(max_length=50, unique=True)
    current_price = models.DecimalField(max_digits=12, decimal_places=4)
    low_price = models.DecimalField(max_digits=12, decimal_places=4)
    high_price = models.DecimalField(max_digits=12, decimal_places=4)
    volume = models.DecimalField(max_digits=12, decimal_places=4)
    created_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.name


class CoinReview(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="my_reviews")
    coin = models.ForeignKey(
        Coin, on_delete=models.PROTECT, related_name="reviews")
    ranking = models.PositiveIntegerField()
    text = models.CharField(
        null=False, default="No comments...", max_length=500)

    def __str__(self) -> str:
        return f"{self.user.get_full_name} - Coin: {self.coin.name}"

    class Meta:
        constraints = [
            constraints.UniqueConstraint(
                fields=["user", "coin"], name="unique user and coin review"),
            constraints.CheckConstraint(check=models.Q(
                ranking__range=(1, 5)), name="check ranking value")
        ]
